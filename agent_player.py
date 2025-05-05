from State import State
import copy
import random
from collections import defaultdict


class q_learning_player:
    def __init__(self, epsilon: float = 0.3):
        self.q_table = defaultdict(lambda: random.uniform(-0.1, 0.1))
        self.epsilon = epsilon

    def choose_action(self, position: State):
        possible_moves = position.possible_moves
        pos_encoding = position.encoding()

        # exploration
        if random.random() < self.epsilon:
            return random.choice(possible_moves)

        # exploitation
        best_move = None
        best_q_val = float("-inf")
        for move in possible_moves:
            key = (pos_encoding, move)
            q_val = self.q_table.get(key, 0)

            if q_val > best_q_val:
                best_move = move
                best_q_val = q_val

        return best_move
    
    def update_q_table(self, item, reward):
        learning_rate = 0.25
        discount_factor = 0.90

        old_q = self.q_table.get(item,0)

        state, move = item
        next_state = copy.deepcopy(state)
        next_state.make_move(move)
        next_possible_moves = next_state.possible_moves

        future_qs = [self.q_table.get((next_state, next_move), 0) for next_move in next_possible_moves]
        max_future_q = max(future_qs) if future_qs else 0

        new_q = old_q + learning_rate * (reward + discount_factor * max_future_q - old_q)

        item = state.encoding(), move
        self.q_table[item] = new_q

    def train(self, num_games=100_000):
        for _ in range(num_games):
            self.epsilon = max(0.1, self.epsilon * 0.99)  # Gradually decay epsilon
            game = State()
            history = []
            while not game.is_terminal:
                opponent_move = random.choice(game.possible_moves)
                game.make_move(opponent_move)
                if game.is_terminal: break

                game_copy = copy.deepcopy(game)
                action = self.choose_action(game)
                history.append((game_copy, action))
                game.make_move(action)

            reward = game.reward()
            discount_factor = 0.85
            for i, item in enumerate(reversed(history)):
                decayed_reward = reward * (discount_factor ** i)
                self.update_q_table(item, decayed_reward)
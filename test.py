from State import State
from agent_player import q_learning_player
import random

def test_q_learning_player(ai_player, num_tests=100):
    win_count = 0
    draw_count = 0
    loss_count = 0
    
    for _ in range(num_tests):
        game = State()
        while not game.is_terminal:
            # Opponent makes a random move
            opponent_move = random.choice(game.possible_moves)
            game.make_move(opponent_move)
            if game.is_terminal: break

            # AI player makes its move
            action = ai_player.choose_action(game)
            game.make_move(action)

        # Check the result of the game
        reward = game.reward()
        if reward == 1:
            win_count += 1
        elif reward == -1:
            loss_count += 1
        else:
            draw_count += 1

    print(f"Win rate: {(win_count / num_tests) * 100}%")
    print(f"Draw rate: {(draw_count / num_tests) * 100}%")
    print(f"Loss rate: {(loss_count / num_tests) * 100}%")


def main():
    # After training
    ai_player = q_learning_player(epsilon=0.1)
    ai_player.train(num_games=100_000)

    # Test the trained AI
    test_q_learning_player(ai_player, num_tests=1000)

if __name__=="__main__":
    main()
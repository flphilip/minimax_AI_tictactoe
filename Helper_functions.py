def out_of_bounds(x, y) -> bool:
    if x > 10 or x < 0: return True
    if y > 7 or y < 0: return True
    return False


def check_direction(starting_indices, x_plus, y_plus, board, player) -> bool:
    field_index_x = starting_indices[0]
    field_index_y = starting_indices[1]
    x = 0
    y = 0
    found_counter = 0
    for i in range(5):
        if out_of_bounds(field_index_x + x, field_index_y + y): return False
        if board[field_index_x + x][field_index_y + y] != player:
            break
        else:
            found_counter += 1
            x += x_plus
            y += y_plus
            if found_counter == 5: return True
    return False

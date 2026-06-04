import random


BOARD_SIZE = 100

SNAKES = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72,
}

LADDERS = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69,
}


def roll_dice():
    return random.randint(1, 6)


def move_player(player, position):
    dice = roll_dice()
    next_position = position + dice

    print(f"{player} rolled a {dice}.")

    if next_position > BOARD_SIZE:
        print(f"{player} needs an exact roll to reach 100.")
        return position

    print(f"{player} moves from {position} to {next_position}.")

    if next_position in LADDERS:
        final_position = LADDERS[next_position]
        print(f"Great! {player} climbed a ladder to {final_position}.")
        return final_position

    if next_position in SNAKES:
        final_position = SNAKES[next_position]
        print(f"Oh no! {player} got bitten by a snake and fell to {final_position}.")
        return final_position

    return next_position


def get_player_count():
    while True:
        value = input("How many players? Enter 2, 3, or 4: ").strip()

        if value in {"2", "3", "4"}:
            return int(value)

        print("Please enter only 2, 3, or 4.")


def create_players(count):
    players = []

    for index in range(1, count + 1):
        name = input(f"Enter player {index} name: ").strip()
        players.append(name or f"Player {index}")

    return players


def print_positions(positions):
    print("\nCurrent positions:")
    for player, position in positions.items():
        print(f"  {player}: {position}")
    print()


def play_game():
    print("Snake and Ladder")
    print("Reach square 100 exactly to win.\n")

    player_count = get_player_count()
    players = create_players(player_count)
    positions = {player: 0 for player in players}

    while True:
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            positions[player] = move_player(player, positions[player])

            if positions[player] == BOARD_SIZE:
                print(f"\n{player} wins the game!")
                return

            print_positions(positions)


if __name__ == "__main__":
    play_game()

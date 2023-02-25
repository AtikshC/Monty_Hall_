import random

# The Monty Hall Game
# - There three closed doors
# - Behind two of the doors there are goats
# - Behind the other door is a brand new car that the contestants want to win
# - Players choose 1 door, then the host, Monty Hall reveals a goat door.
# - Then the player is given the option to switch their choice to the other unopened door, or stay with their original choice
# - Intuitively most people think that after the goat door is opened, there is a 50-50 chance,
# - however, this simulator will show that the odds of winning become 2/3 to 1/3 if you switch.
# We will create a simulator to show the number of times a player will win and lose, after playing N rounds


# Input : N, the number of times the game will be played, switch, boolean, that says if the player chooses to switch or not each time.
# Output: (wins, losses) - wins is the number of times out of N we won the car, and losses, is the number of times we lost out of N, so wins + losses = N
# Run one round of the monty hall game.
# choice - the door we choose, 0 <= choice <= 2
# This will return True if we win, False if we lose
def monty_hall(choice, switch):

    # Step 1: Create the 3 doors, figure out behind which doors the goats and the car are. Use random to map 'g' for goat, and 'c' for car behind the doors
    prizes = ['g', 'g', 'c']  # goat, goat, car
    random.shuffle(prizes)
    doors = [0, 1, 2]
    mappings = list(zip(doors, prizes))
    mapPrizesToDoors = {m[0]: m[1] for m in mappings}
    #print(mapPrizesToDoors)

    # Step 2: Store the choice that the player made in door_selected
    door_selected = choice
    #print(f"door selected: {door_selected}")
    
    # Step 3: Monty Hall opens a door with a goat behind it, the chosen door cannot be the one the player selected.
    
    doorOpeningChoices = list(filter(lambda door : (mapPrizesToDoors[door] == 'g' and door != door_selected), mapPrizesToDoors.keys()))  # We want to get indices of doors that have a goat behind it AND it has not been chosen

    #print(doorOpeningChoices)

    # Monty Hall randomly chooses one of the doors from doorOpeningChoices
    open_door_choice = doorOpeningChoices[random.randint(0, len(doorOpeningChoices)-1)]
    #print(open_door_choice)

    # Step 4: The players sees this door, and decides, whether they want to switch or not, determined by the switch parameter.
    if switch:
        door_selected = list(filter(lambda door : (door != open_door_choice and door != door_selected), mapPrizesToDoors.keys()))[0]

    #print(f"door selected: {door_selected}")
    # Step 5: We reveal the door_selected, and if they won a car, return True, else return False.
    return mapPrizesToDoors[door_selected] == "c"


def run_mh_n_times(rounds, switch):
    wins = 0
    losses = 0
    for i in range(rounds):
        outcome = monty_hall(random.randint(0, 2), switch)
        if outcome:
            wins += 1
        else:
            losses += 1

    return (wins, losses)

result = run_mh_n_times(1000, False)

print(f"Wins: {result[0]}, Losses: {result[1]}")
num_lines = 0
master_sum = 0

# Open a document
doc = open('input.txt', 'rt')

for line in doc:
    # Read a line
    num_lines = num_lines + 1

    # set up the game
    valid_game = True

    # Determine the game ID and store it

    # Split the line into title and pulls
    temp = line.split(":")
    title = temp[0]
    tmp2 = temp[1]

    print(f"Game Title: {title}")
    temp = title.split(" ")
    game_id = int(temp[1])

    # Split the games
    pulls = tmp2.split(";")
    print('-----------------------')
    print(line)

    min_red = 0
    min_green = 0
    min_blue = 0

    # Analyze each pull and determine the minimum number of each color cube to make the pull valid
    for pull in pulls:

        # for the pull, divide the cubes
        cubes = pull.split(",")

        # for each cube determine the color and the count
        for cube in cubes:
            cube = cube.strip() # first cube has an extra space
            pair = cube.split(" ")
            color = pair[1]
            count = pair[0]

            # now compare the color's count against the max color value. If greater, the game is invalid
            match color:
                case 'blue':
                    if int(count) > min_blue:
                        min_blue = int(count)
                case 'green':
                    if int(count) > min_green:
                        min_green = int(count)
                case 'red':
                    if int(count) > min_red:
                        min_red = int(count)

        print(f"current mins are red: {min_red}, green {min_green}, blue {min_blue}")

    # Now the min values should be set, so multiply them together to get the Game sum
    game_product = min_red * min_green * min_blue
    print(f"Game {game_id}'s product is {game_product}")

    # Add this game's product to the master sum
    master_sum = master_sum + game_product

# Close the document
doc.close()

# print the master number
print(f'The sum of the IDs of the games is {master_sum} based on {num_lines} lines')
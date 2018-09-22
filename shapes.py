'''
This application allows users to draw 4 different shapes. The size of the shape is
determined by the user input.
'''

# SHAPE 1: RIGHT ANGLE TRIANGLE
def draw_right_angle_triangle():
    print()
    rows = int(input('Enter the number of rows: '))

    # Outer FOR loop to print amount of rows
    # starting from 1 the range of rows is given by user input in this case
    for row in range(1, rows+1):
        # inner loop to print the columns as "*"
        # the END arg is used so the stars will be printed on the same line
        for col in range(1, row+1):
            print('* ', end='')
        # print statement to start new row
        print()

# draw_right_angle_triangle()

# SHAPE 2: LEFT ANGLE TRIANGLE
def draw_left_angle_triangle():
    rows = int(input('Enter the number of rows: '))
    spaces = 2 * rows - 2

    # Outer FOR loop to print amount of rows
    # starting from 1 the range of rows is given by user input in this case
    for row in range(0, rows):
        # inner loop the create spaces
        for space in range(0, spaces):
            print(end=' ')

        # decrementing spaces after each loop
        spaces -= 2

        for col in range(0, row+1):
            print('* ', end='')
        print()

# SHAPE 3: PYRAMID
def draw_pyramid():
    rows = int(input('Enter the number of rows for pyramid: '))

    # Loop to print out new rows
    for row in range(0, rows):
        # print spaces on the leftside
        for space in range(0, rows-row-1):
            print(end=' ')
        
        # Print * and spaces to shape the pyramid
        for col in range(0, row+1):
            print('* ', end='')
        
        # Start new row
        print()

# SHAPE 4: DIAMOND
def draw_diamond():
    rows = int(input('Enter the amount of rows: '))
    
    # rows ranges according to user input
    for top_rows in range(rows):
        print(' ' * (rows-top_rows-1) + '* ' * (top_rows+1))
    
    # reverse pyramid loop. Starting from "rows" -1 to 0.
    # decrementing by 1 to print the amount of stars
    for low_rows in range(rows-1,0,-1):
        print(' ' * (rows-low_rows) + '* ' *(low_rows))

play_game = True

# Play game untill user types in q
while play_game:
    print()
    print('(1) ~ Right Angle Triangle')
    print('(2) ~ Left Angle Triangle')
    print('(3) ~ Pyramid')
    print('(4) ~ Diamond')
    print()
    choice = input('Choose a shape you\'d like me to draw or type "q" to quit: ')
    print('')

    if choice == "1":
        draw_right_angle_triangle()
    elif choice == "2":
        draw_left_angle_triangle()
    elif choice == "3":
        draw_pyramid()
    elif choice == "4":
        draw_diamond()
    elif choice == 'q':
        play_game = False
    

    
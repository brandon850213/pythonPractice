# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

star = '*'
blank = ' '

for row in picture:
    for pixel in row:
        if pixel:
            print(star, end=' ')
            # change the default value of print end to make sure print in same line
        else:
            print(blank, end=' ')
    print('')  # print new line after each row

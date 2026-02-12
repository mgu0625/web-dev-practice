def print_row(bricks, height):
    spaces = height - bricks

    for _ in range(spaces):
        print(" ", end="")

    #print bricks
    for _ in range(bricks):
        print("#", end="")

    print()


def main():
    # get input + check for validation    
    while True:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    
    #print out the #'s
    for i in range(height):
        print_row(i + 1, height)
    


main()
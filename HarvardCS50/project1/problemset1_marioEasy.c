#include <cs50.h>
#include <stdio.h>

void print_row(int bricks, int height);

int main(void)
{
    // for incorrect input
    int height;
    do
    {
        height = get_int("What is height of pyramid? ");
    }
    while (height <= 0 || height > 8);

    // print height
    for (int i = 0; i < height; i++)
    {
        print_row(i + 1, height);
    }
}

// inputting number of bricks
void print_row(int bricks, int height)
{
    int spaces = height - bricks;

    // to make it right sided
    for (int i = 0; i < spaces; i++)
    {
        printf(" ");
    }

    // to print out #'s
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}

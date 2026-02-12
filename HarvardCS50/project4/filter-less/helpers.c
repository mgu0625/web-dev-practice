#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop through rows
    for (int row = 0; row < height; row++)
    {
        // loop through columns
        for (int column = 0; column < width; column++)
        {
            int red = image[row][column].rgbtRed;
            int green = image[row][column].rgbtGreen;
            int blue = image[row][column].rgbtBlue;

            // round out the values of each pixel
            int avg = (int) round((red + green + blue) / 3.0);

            // change pixel color to new color
            image[row][column].rgbtRed = avg;
            image[row][column].rgbtGreen = avg;
            image[row][column].rgbtBlue = avg;
        }
    }
}

// helper function for sepia function
int clamp(int value)
{
    if (value > 255)
    {
        return 255;
    }
    return value;
}

// Convert image to sepia (warm brown-gold color filter, gives vintage look)
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // loop through rows
    for (int row = 0; row < height; row++)
    {
        // loop through columns
        for (int column = 0; column < width; column++)
        {
            int red = image[row][column].rgbtRed;
            int green = image[row][column].rgbtGreen;
            int blue = image[row][column].rgbtBlue;

            // make the sepia color for each pixel
            int sepiaRed = clamp(round(.393 * red + .769 * green + .189 * blue));
            int sepiaGreen = clamp(round(.349 * red + .686 * green + .168 * blue));
            int sepiaBlue = clamp(round(.272 * red + .534 * green + .131 * blue));


            // change pixel color to sepia color
            image[row][column].rgbtRed = sepiaRed;
            image[row][column].rgbtGreen = sepiaGreen;
            image[row][column].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // loop through rows
    for (int row = 0; row < height; row++)
    {
        // loop through columns
        for (int column = 0; column < width / 2; column++)
        {
            // store the left column in a temporary variable;
            RGBTRIPLE temp = image[row][column];

            // move to right column in the left spot
            image[row][column] = image[row][width - column - 1];

            // move to left column in the right spot
            image[row][width - column - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // create copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i ++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    // blur each pixel using copy
    // loop through rows
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            // initialize variables
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;

            int counter = 0;

            // loop through surrounding pixels for each pixel 
            //for 3x3 grid
            for (int di = -1; di < 2; di++)
            {
                for (int dj = -1; dj < 2; dj++)
                {
                    int ni = row + di;
                    int nj = column + dj;

                    // skip neighbors that are out of bounds
                    if (ni < 0 || ni >= height || nj < 0 || nj >= width)
                    {
                        continue;
                    }

                    // add to the sum
                    sumRed += copy[ni][nj].rgbtRed;
                    sumGreen += copy[ni][nj].rgbtGreen;
                    sumBlue += copy[ni][nj].rgbtBlue;

                    counter ++;
                }
            }

            // add blur effect to original image
            image[row][column].rgbtRed = (int) round((float) sumRed / counter);
            image[row][column].rgbtGreen = (int) round((float) sumGreen / counter);
            image[row][column].rgbtBlue = (int) round((float) sumBlue / counter);
        }
    } 

}

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
            RBTRIPLE temp = image[row][column];

            // move to right column in the left spot
            image[row][column] = image[row][width - column - 1];

            // move to left column in the right spot
            image[row][width - column - 1] = temp;
        }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // declare image variable
    RGBTRIPLE temp[height][width];

    // loop through rows
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            // duplicate original image
            temp[row][column] = image[row][column];
        }
    }

    

}

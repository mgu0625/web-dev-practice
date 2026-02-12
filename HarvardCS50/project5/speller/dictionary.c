// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table
const unsigned int N = 1009;

// count for the number of words in the dictionary
unsigned int counter =0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // hash the word to obtain a hash value
    unsigned int index = hash(word);
    // cursor to move through the linked lists
    node *cursor = table[index];
    //access linked at the index in the hash table and traverse
    while (cursor != NULL)
    {
        // If the word is found return true, else move cursor to the next node
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    // hash the word 
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long h = 5381;
    // Improve this hash function
    for (int c = *word; c != '\0'; c = *++word)
    {
        c = tolower((unsigned char) c);
        h = ((h << 5) + h) + c;
    }
    return (unsigned int)(h % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // open a dictionary file
    FILE *file = fopen(dictionary, "r");


    if (file == NULL)
    {
        return false;
    }

    // initialize table
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    counter = 0;

    char buffer[LENGTH + 1];

    // read strings from file one at a time
    while (fscanf(file, "%s", buffer) != EOF)
    {
        // allocate new memory
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(file);
            return false;
        }

        // copy word into node
        strcpy(n->word, buffer);

        // hash word to obtain a hash value
        unsigned int index = hash(buffer);

        // insert node into hash table in the corresponding bucket
        n->next = table[index];
        table[index] = n;

        // increment only after success
        counter++;
    }

    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }

        table[i] = NULL;
    }

    counter = 0;
    return true;
}

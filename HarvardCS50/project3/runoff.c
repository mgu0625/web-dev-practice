/**
Week 3 Project 3: Runoff. 
Spring 26'
*/
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    // from typedef struct
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // checking every candidate to see if it matches
    for (int i = 0; i < candidate_count; i++)
    {
        // if user input matches candidate name exactly
        if (strcmp(name, candidates[i].name) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // process one voter at a time
    for (int i = 0; i < voter_count; i++)
    {
        // scanning votes for ranks
        for (int j = 0; j < candidate_count; j++)
        {
            // convert stored preference to candidate index
            int candidate_index = preferences[i][j];

            // count vote if candidate is not elimitated
            if (!candidates[candidate_index].eliminated)
            {
                candidates[candidate_index].votes++;

                // break if vote is assigned
                break;
            }
        }
    }

    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    for (int i = 0; i < candidate_count; i++)
    {
        int mostVote = voter_count / 2;

        if (candidates[i].votes > mostVote)
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }

    // return false if there's no winner
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int minor_vote = candidates[0].votes;

    // repeat per candidate
    for (int i = 0; i < candidate_count; i++)
    {
        // check for elimination
        if (!candidates[i].eliminated && candidates[i].votes < minor_vote)
        {
            minor_vote = candidates[i].votes;
        }
    }
    

    // return that program succeeded
    return minor_vote;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{   
    for (int i = 0; i < candidate_count; i++)
    {
        // check if candidate is NOT eliminated
        // skip eliminated candidates
        // check if candidate has different number of votes than minimum
        // if yes -> not tie, if no -> tie
        if (!candidates[i].eliminated && candidates[i].votes != min)
        {
            return false;
        }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if candidate has the lowest number of votes and eliminate that candidate
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
    return;
}

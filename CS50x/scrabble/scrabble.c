#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int points(string word);

int main(void) {
    string players[2];
    players[0] = get_string("Player 1: ");
    players[1] = get_string("Player 2: ");

    if (points(players[0]) > points(players[1])) {
        printf("Player 1 wins!\n");
    }
    else if (points(players[0]) < points(players[1])) {
        printf("Player 2 wins!\n");
    }
    else {
        printf("Tie!\n");
    }
}


int points(string word) {
    int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int score = 0;

    for (int i = 0; word[i] != '\0'; i++) {
        char letter = toupper(word[i]);

        if (letter >= 'A' && letter <= 'Z') {
            int letter_index = letter - 'A'; // Obter a posição da letra em POINTS

            score += POINTS[letter_index];
        }
    }
    return score;
}


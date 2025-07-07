#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <math.h>

void grade(int index);
int count(string sample);

int main(void) {
    string text = get_string("Text: ");
    grade(count(text));

}


void grade(int index) {
    if (index >= 16) {
        printf("Grade 16+\n");
    }
    else if (index < 1) {
        printf("Before Grade 1\n");
    }
    else {
        printf("Grade %d\n", index);
    }
}

int count(string sample) {
    int letter = 0;
    int word = 1;
    int sentence = 0;
    int i = 0;
    while(sample[i] != '\0') {
        //Count letters
        if (isalpha(sample[i])) {
            letter++;
        }
        //Count words
        else if (sample[i] == ' ' && sample[i -1] != ' ') {
            word++;
        }
        //Count sentences
        else if (sample[i] == '.' || sample[i] == '!' || sample[i] == '?') {
            sentence++;
        }
        i++;
    }
    // Calculate average number of letters per 100 words
    float aver_l = ((float)letter / word) * 100;
    // Calculate average number of sentences per 100 words
    float aver_s = ((float)sentence / word) * 100;
    // Calculate the Coleman-Liau index (rounded)
    int index = round(0.0588 * aver_l - 0.296 * aver_s - 15.8);

    return index;
}

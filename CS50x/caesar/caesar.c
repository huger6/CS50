#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

void encrypt(char txt[], int key);


int main(int argc, string argv[]) {
    if (argc != 2) {
        printf("Usage: ./caesar key");
        return 1;
    }

    int i = 0;
    int len = strlen(argv[1]);
    while ( i < len) {
        if (!isdigit(argv[1][i])) {
            printf("Usage: ./caesar key");
            return 1;
        }
        i++;
    }

    string text = get_string("plaintext:  ");
    //text is being converted
    encrypt(text, atoi(argv[1]));

    printf("ciphertext: %s\n", text);
    return 0;
}


void encrypt(char txt[], int key) {
    int len = strlen(txt);

     for (int i = 0; i < len; i++) {
        if (txt[i] >= 'a' && txt[i] <= 'z') {
            // Encrypt lowercase letters
            txt[i] = 'a' + (txt[i] - 'a' + key) % 26;
        } else if (txt[i] >= 'A' && txt[i] <= 'Z') {
            // Encrypt uppercase letters
            txt[i] = 'A' + (txt[i] - 'A' + key) % 26;
        }
    }
}

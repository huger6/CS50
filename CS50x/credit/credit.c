#include <cs50.h>
#include <stdio.h>
#include <math.h>

int check_length(long num);
bool validation(long num);
bool amex(long num, int len);
bool mastercard(long num, int len);
bool visa(long num, int len);


int main(void) {
    long cc;
    do
    {
        cc = get_long("Number: ");
    } while (cc <= 0);

    int len = check_length(cc);
    if (!validation(cc)) {
        printf("INVALID\n");
    }
    else {
        if (len == 13 && visa(cc, 13)) {
            printf("VISA\n");
        } else if (len == 15 && amex(cc, 15)) {
            printf("AMEX\n");
        } else if (len == 16) {
            if (mastercard(cc, 16)) {
                printf("MASTERCARD\n");
            } else if (visa(cc, 16)) {
                printf("VISA\n");
            } else {
                printf("INVALID\n");
            }
        } else {
            printf("INVALID\n");
        }
    }
}


int check_length(long num) {
    int length = 0;
    if (num == 0) {
        return 0; // Não se verifica - 0 (F)
    }
    else if (num < 0) {
        return 0;
    }
    while (num != 0) {
        num /= 10;
        length++;
    }

        return length;
    }


bool validation(long num) {
    int sum = 0;
    int digit;
    int should_double = 0;

    while (num > 0) {
        digit = num % 10;
        num /= 10;

        if (should_double) { // esta afirmação verifica se should_double é diferente de 0
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        should_double = !should_double;
    }
    return (sum % 10 == 0);
}

bool amex(long num, int len) {
    num /= pow(10, len - 2);
    if (num == 34 || num == 37) {
        return 1;
    }
    else {
        return 0;
    }
}

bool mastercard(long num, int len) {
    num /= pow(10, len - 2);
    if (num == 51 || num == 52 || num == 53 || num == 54 || num == 55) {
        return 1;
    }
    else {
        return 0;
    }
}


bool visa(long num, int len) {
    num /= pow(10, len - 1);
    if (num == 4) {
        return 1;
    }
    else {
        return 0;
    }
}

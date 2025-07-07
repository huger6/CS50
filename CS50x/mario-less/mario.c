#include <stdio.h>
#include <cs50.h>

void row(int bricks, int height);

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    for (int i = 1; i <= n; i++)
    {
        row(i, n);
    }
}

void row(int bricks, int height)
{
    for(int i = 0; i < height - bricks; i++)
    {
                printf(" ");
    }
    for(int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}



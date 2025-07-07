// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    //atof converts string to double
    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    //Buffer with HEADER_SIZE size
    uint8_t header[HEADER_SIZE];
    //If file can be read
    fread(header, HEADER_SIZE, 1, input);
    //Copy the first 44 bytes (header)
    fwrite(header, HEADER_SIZE, 1, output);

    // TODO: Read samples from input file and write updated data to output file

    // Create a buffer for a single sample
    int16_t buffer;

    // Read single sample from input into buffer while there are samples left to read
    while (fread(&buffer, sizeof(int16_t), 1, input))
    {
        // Update volume of sample
        buffer *= factor;
        // Write updated sample to new file
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }
    //Close files
    fclose(input);
    fclose(output);
    return 0;
}

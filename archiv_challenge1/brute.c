#include "stdio.h"
#include <openssl/sha.h>
#include <stdbool.h> 
#include <string.h>
#include <stdlib.h>

char guess[] = "000000";
//37 29 42 df 27 12 82 45 05 d8 17 1f 4f 0b cb 14 15 3d 39 ba
char answer[] = {"\x37\x29\x42\xdf\x27\x12\x82\x45\x05\xd8\x17\x1f\x4f\x0b\xcb\x14\x15\x3d\x39\xba"};

void RotChar()
{
    bool keepGoing = true;
    int i = 0;
    while(keepGoing)
    {
        keepGoing = false;
        guess[i] = guess[i] + 1;
        if(guess[i] == ':')
        {
            guess[i] = 'A';
        }
        if(guess[i] == '[')
        {
            guess[i] = '0';
            keepGoing = true;
            i++;
        }
    }
}

//magic sequence
//0 7 14 1 8 15 2 9 16 3 10 17 4 11 18 5 12 19 6 13 
void Pseudorand(char *output, char *key)
{
    output[0] = key[0];
    output[1] = key[7];
    output[2] = key[14];
    output[3] = key[1];
    output[4] = key[8];
    output[5] = key[15];
    output[6] = key[2];
    output[7] = key[9];
    output[8] = key[16];
    output[9] = key[3];
    output[10] = key[10];
    output[11] = key[17];
    output[12] = key[4];
    output[13] = key[11];
    output[14] = key[18];
    output[15] = key[5];
    output[16] = key[12];
    output[17] = key[19];
    output[18] = key[6];
    output[19] = key[13];
}

int main()
{
    unsigned char stage1[SHA_DIGEST_LENGTH];
    unsigned char stage2[SHA_DIGEST_LENGTH];
    unsigned char stage3[SHA_DIGEST_LENGTH];

    double i = 0;

    while(true)
    {
        i++;
        RotChar();

        //stage1 = sha1(guess)
        SHA1(guess, 6, stage1);

        //stage2 = pseudo(stage1)
        Pseudorand(stage2, stage1);

        //stage3 = sha1(stage2)
        SHA1(stage2, SHA_DIGEST_LENGTH, stage3);

        if(memcmp(answer, stage3, SHA_DIGEST_LENGTH) == 0)        
        {
            printf("WIN:\n%s\n", guess);
            exit(0);
        }
        else
        {
            if((((int)i) % 1000000) == 0)
            {
                printf("%f%% complete\n", (double)((i*100)/2176782336.0));
                printf("\tguess: %s\n", guess);
            }
        }
    }
}


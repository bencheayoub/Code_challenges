#include <string.h>

void moveTen(char *str){

    for(int i = 0; i < strlen(str); i++)
    {
        if((str[i] <= 'p' && str[i] >='a')||(str[i] >= 'A' && str[i] <= 'P'))
        {
            str[i] += 10;
        }
        else if((str[i] > 'p' && str[i] <= 'z')||(str[i] > 'P' && str[i] <= 'Z'))
        {
            str[i] -= 16;
        }
    }

}

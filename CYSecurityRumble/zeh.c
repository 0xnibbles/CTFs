#include <stdio.h>
#include <stdlib.h>
//#include "fahne.h"

void main(void) {
    int e = rand();
    int flag = 53225;
    int k = 0;
    int initial_k = 0;

    printf("Value for k\n");
    scanf("%d", &k);

    initial_k = k;
    for (int i = 7; i--;)
        k = e >> (k % 3);

    e = (k) ^ (flag);

    printf("k = %d and e = %d\n",initial_k,e);
}

// about rand without seeding it - https://stackoverflow.com/questions/1108780/why-do-i-always-get-the-same-sequence-of-random-numbers-with-rand
// shifting operations - https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/

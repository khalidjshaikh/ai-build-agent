#include <stdio.h>

#ifndef BUILD_NUMBER
#define BUILD_NUMBER 0
#endif

int main(void) {
    printf("Hello, world! Build %d\n", BUILD_NUMBER);
    return 0;
}

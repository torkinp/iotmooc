#include <stdio.h>

int fib(int x, int y) {
    return x + y;
}

int main() {
    int fx = -1;
    int fy = 1;
    int res = 0;
    int i;

    for(i = 1; i<=6; i++) {
        res = fib(fx, fy);
        printf("%i:   %i\n", i, res);
        fx = fy;
        fy = res;
    }
    
    return;
}

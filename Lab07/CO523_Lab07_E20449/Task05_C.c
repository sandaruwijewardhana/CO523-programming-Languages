#include <stdio.h>

int f(int a) {
    int b = a + 2;
    return b;
}

int g() {
    int x = 3;
    int y = f(x);
    return y;
}

int main() {
    int result = g();
    printf("Result: %d\n", result);
    return 0;
}

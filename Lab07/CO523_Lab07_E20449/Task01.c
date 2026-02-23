// Task 01 - C (pass-by-value)

#include <stdio.h>

void modify(int x) {
    x = x + 10;
    printf("Inside function: %d\n", x);
}

int main() {
    int a;
    printf("Enter an integer: ");
    scanf("%d", &a);

    printf("Before function: %d\n", a);

    modify(a);

    printf("After function: %d\n", a);
    return 0;
}
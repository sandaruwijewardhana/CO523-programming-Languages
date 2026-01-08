#include <ctype.h>
#include <stdlib.h>
#include <stdio.h>

/* Global variable to hold the current input character/token */
int token; 

/* Function prototypes for recursive descent */
void command();
int expr();
int term();
int factor();
int number();
int digit();

void error(char* message) {
    printf("Parse error: %s\n", message);
    exit(1);
}

void getToken() {
    token = getchar();
}

void match(char c, char* message) {
    if (token == c) {
        getToken();
    } else {
        error(message);
    }
}

void command() {
    
    int result = expr();
    if (token == '\n' || token == EOF) {
        printf("The result is: %d\n", result);
    } else {
        error("Tokens remaining after end of expression");
    }
}

int expr() {
    int result = term();
    while (token == '+' || token == '-') {
        char op = token;
        match(op, "Expected + or -");
        int rhs = term();

        if (op == '+') result = result + rhs;
        else result = result - rhs;
    }
	 
    return result;
}

int term() {
    int result = factor();
    while (token == '*' || token == '/') {
        char op = token;
        match(op, "Expected * or /");
        int rhs = factor();

        if (op == '*') result = result * rhs;
        else {
            if (rhs == 0) error("Division by zero");
            result = result / rhs; 
        }
    }

    return result;
}

int factor() {
    if (token == '(') {
        match('(', "Expected '('");
        int result = expr();
        match(')', "Expected ')'");
        return result;
    } else {
        return number();
    }
}

int number() {
    int result = digit();
    while (isdigit(token)) {
        result = result * 10 + digit();
    }

    return result;
}

int digit() {
    /* digit -> '0' | '1' | ... | '9' */
    int result;
    if (isdigit(token)) {
        result = token - '0';
        /* Pass the current token to match so it moves to next character */
        match(token, "digit expected"); 
    } else {
        error("digit expected");
    }
    return result;
}

void parse() {
    getToken(); /* Initialize the first token */
    command();  /* Start parsing from the top-level symbol */
}

int main() {
    printf("Enter a math expression (e.g., 2+3*4): ");
    parse();
    return 0;
}

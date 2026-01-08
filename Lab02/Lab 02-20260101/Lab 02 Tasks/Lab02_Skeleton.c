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
	
    /* TODO: Implement grammar rule: <expr> ::= <term> + <term> | <term> - <term> | <term> 
     * 1. get the first operand.
     * 2. check if 'token' is '+' or '-'.
     * 3. match the operator and call term() again.
     * 4. Perform the operation.
     */
	 
    return result;
}


int term() {
    /* TODO: Implement grammar rule: <term> ::= <factor> * <factor> | <factor> / <factor> | <factor> 
     Same logic as method 'int expr()'
     */
}


int factor() {
    /* TODO: Implement grammar rule: <factor> ::= ( <expr> ) | <number> 
     * 1. Check if the current 'token' is a '('.
     * - If yes: match '(', call expr(), then match ')'.
     * 2. If it is not '(', call number().
     */
}

int number() {
    /* TODO: Implement grammar rule: <number> ::= <digit> <number> | <digit>
	 * 1. Call digit() to get the first digit.
     * 2. Use a while loop to check if 'token' is currently a digit (isdigit(token)).
     * 3. If yes, update result: result = result * 10 + digit()
     */*/
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

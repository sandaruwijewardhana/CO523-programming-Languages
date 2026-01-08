#include <stdio.h>
#include <string.h>

#define MAX_ACCOUNTS 100 // Maximum number of accounts the bank can hold
#define MAX_OWNER_NAME_LENGTH 50

// Define the BankAccount structure
typedef struct {
    int account_number;
    char owner[MAX_OWNER_NAME_LENGTH];
    double balance;
    int is_active; // Flag to indicate if the slot is used (replaces dict key existence)
} BankAccount;

// Global array to store all bank accounts
BankAccount accounts[MAX_ACCOUNTS];

// Global variable to keep track of the number of active accounts
int account_count = 0;

// --- Helper Function ---

// Function to find an account by number. Returns the index or -1 if not found.
int find_account_index(int account_number) {
    for (int i = 0; i < account_count; i++) {
        if (accounts[i].is_active && accounts[i].account_number == account_number) {
            return i; // Account found at index i
        }
    }
    return -1; 
}

// --- Core Bank Functions (Procedural) ---

// Function to initialize the bank (optional, but good practice)
void init_bank() {
    // Set all account slots to inactive
    for (int i = 0; i < MAX_ACCOUNTS; i++) {
        accounts[i].is_active = 0;
    }
    account_count = 0;
    printf("Bank system initialized.\n");
}

// Function to create an account
void create_account(int account_number, const char* owner, double initial_balance) {
    if (account_count < MAX_ACCOUNTS) {
        accounts[account_count].account_number = account_number;
        strncpy(accounts[account_count].owner, owner, MAX_OWNER_NAME_LENGTH);
        accounts[account_count].balance = initial_balance;
        accounts[account_count].is_active = 1;
        account_count++;
        printf("Created account %d for %s with balance %.2f\n", account_number, owner, initial_balance);
    } else {
        printf("Error: Maximum account limit reached.\n");
    }
}

// Function to deposit money
void deposit(int account_number, double amount) {
    int index = find_account_index(account_number);
    if (index != -1) {
        accounts[index].balance += amount;
        printf("[%d] Deposited %.2f. New balance = %.2f\n", account_number, amount, accounts[index].balance);
    } else {
        printf("Account not found.\n");
    }
}

// Function to withdraw money
void withdraw(int account_number, double amount) {
    int index = find_account_index(account_number);
    if (index != -1) {
        if (accounts[index].balance >= amount) {
            accounts[index].balance -= amount;
            printf("[%d] Withdrawn %.2f. New balance = %.2f\n", account_number, amount, accounts[index].balance);
        } else {
            printf("Insufficient funds.\n");
        }
    } else {
        printf("Account not found.\n");
    }
}

// Function to show balance
void show_balance(int account_number) {
    int index = find_account_index(account_number);
    if (index != -1) {
        printf("[%d] Owner: %s, Balance: %.2f\n", account_number, accounts[index].owner, accounts[index].balance);
    } else {
        printf("Account not found.\n");
    }
}

// --- Main Method ---

int main() {
    init_bank();

    printf("--- Starting Bank System (Default Package) ---\n");

    create_account(101, "Ruwan", 1000.00);
    create_account(102, "Nimal", 500.00);

    printf("--- Transactions ---\n");
    
    deposit(101, 300.00);
    withdraw(102, 100.00);

    printf("--- Final Balances ---\n");
    show_balance(101);
    show_balance(102);
    show_balance(999); 

    return 0;
}

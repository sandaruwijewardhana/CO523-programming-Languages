import java.util.ArrayList;
import java.util.List;

public class BankApp {
    // Stores accounts using a List
    private static List<BankAccount> accounts = new ArrayList<>();

    // --- Helper Method to find account using Linear Search ---
    private static BankAccount findAccount(int accountNumber) {
        for (BankAccount account : accounts) {
            if (account.getAccountNumber() == accountNumber) {
                return account;
            }
        }
        return null;
    }

    // Function to create and add an account
    public static BankAccount createAccount(int accountNumber, String owner, double balance) {
        // Check if account already exists
        if (findAccount(accountNumber) != null) {
            System.out.println("Account already exists.");
            return null;
        }
        // Create a new BankAccount object and add it to the 'accounts' list
        BankAccount newAccount = new BankAccount(accountNumber, owner, balance);
        accounts.add(newAccount);
        System.out.printf("Created account %d for %s with balance %.2f\n", accountNumber, owner, balance);
        return newAccount;
    }

    // Function to handle deposit
    public static void deposit(int accountNumber, double amount) {
        BankAccount account = findAccount(accountNumber);
        if (account != null) {
            account.deposit(amount);
        } else {
            System.out.println("Account not found.");
        }
    }

    // Function to handle withdrawal
    public static void withdraw(int accountNumber, double amount) {
        BankAccount account = findAccount(accountNumber);
        if (account != null) {
            account.withdraw(amount);
        } else {
            System.out.println("Account not found.");
        }
    }

    // Function to show balance
    public static void showBalance(int accountNumber) {
        BankAccount account = findAccount(accountNumber);
        if (account != null) {
            account.showBalance();
        } else {
            System.out.println("Account not found.");
        }
    }

    // Main Method
    public static void main(String[] args) {
        System.out.println("--- Starting Bank System (Default Package) ---");
        
        createAccount(101, "Ruwan", 1000.00);
        createAccount(102, "Nimal", 500.00);
        
        System.out.println("--- Transactions ---");
        
        deposit(101, 300.00);
        withdraw(102, 100.00);
        
        System.out.println("--- Final Balances ---");
        showBalance(101);
        showBalance(102);
        showBalance(999);  // Account not found
    }
}

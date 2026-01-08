public class BankAccount {
    // Attributes
    private final int accountNumber; 
    private final String owner;
    private double balance;

    // Constructor
    public BankAccount(int accountNumber, String owner, double balance) {
        this.accountNumber = accountNumber;
        this.owner = owner;
        this.balance = balance;
    }

    // Operation: Deposit
    public void deposit(double amount) {
        this.balance += amount;
        System.out.printf("[%d] Deposited %.2f. New balance = %.2f\n", this.accountNumber, amount, this.balance);
    }

    // Operation: Withdraw
    public void withdraw(double amount) {
        if (this.balance >= amount) {
            this.balance -= amount;
            System.out.printf("[%d] Withdrawn %.2f. New balance = %.2f\n", this.accountNumber, amount, this.balance);
        } else {
            System.out.println("Insufficient funds.");
        }
    }

    // Operation: Show Balance
    public void showBalance() {
        System.out.printf("[%d] Owner: %s, Balance: %.2f\n", this.accountNumber, this.owner, this.balance);
    }

    // Getter for account number
    public int getAccountNumber() {
        return this.accountNumber;
    }
}

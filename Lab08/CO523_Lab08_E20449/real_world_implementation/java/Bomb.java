// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — Bomb (Concrete Weapon)
//
// Inheritance + Abstraction: Bomb extends the abstract Weapon class and provides
// its own implementation of deploy(). It represents one of the two weapon types
// available from the Seller (category="Clemo", duration=12.00).

public class Bomb extends Weapon {
    private final String category;  // Type/category of the bomb
    private final float duration;   // Time (in seconds) to activate the bomb

    public Bomb(String category, float duration) {
        this.category = category;
        this.duration = duration;
    }

    public String getCategory() {
        return category;
    }

    public float getDuration() {
        return duration;
    }

    // Overrides abstract deploy() — prints the bomb's activation time
    @Override
    public void deploy() {
        System.out.println("Bomb activation time: " + duration + " seconds");
    }
}

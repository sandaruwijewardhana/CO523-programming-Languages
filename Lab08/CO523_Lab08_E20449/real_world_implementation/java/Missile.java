// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — Missile (Concrete Weapon)
//
// Inheritance + Abstraction: Missile extends the abstract Weapon class and provides
// its own implementation of deploy(). It is the second weapon type available
// from the Seller (code="0001", range="Intercontinental", type="nuclear").

public class Missile extends Weapon {
    private final String code;   // Missile identification code
    private final String range;  // Range category (e.g., Intercontinental)
    private final String type;   // Warhead type (e.g., nuclear)

    public Missile(String code, String range, String type) {
        this.code = code;
        this.range = range;
        this.type = type;
    }

    public String getCode() {
        return code;
    }

    public String getRange() {
        return range;
    }

    public String getType() {
        return type;
    }

    // Overrides abstract deploy() — prints launch readiness message
    @Override
    public void deploy() {
        System.out.println("Missile ready for launch");
    }
}

// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — GlobalTerrorist (Concrete Subclass)
//
// Inheritance + Polymorphism: GlobalTerrorist extends the abstract Terrorist class.
// It overrides attack() to print the country it targets, and compromise() to return
// the code name — used when the agent catches the terrorist.

public class GlobalTerrorist extends Terrorist {
    private final String codeName; // Alias used in international operations
    private final String country; // Target country for the attack

    public GlobalTerrorist(String codeName, String country) {
        this.codeName = codeName;
        this.country = country;
    }

    public String getCodeName() {
        return codeName;
    }

    public String getCountry() {
        return country;
    }

    // Overrides abstract attack() — global terrorists attack a specific country
    @Override
    public void attack() {
        System.out.println("Attacking country: " + country);
    }

    // Overrides abstract compromise() — returns code name when caught by the agent
    @Override
    public String compromise() {
        return codeName;
    }
}

// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — LocalTerrorist (Concrete Subclass)
//
// Inheritance + Polymorphism: LocalTerrorist extends the abstract Terrorist class.
// It overrides attack() to print the city it targets, and compromise() to return
// the real name — used when the agent catches the terrorist.

public class LocalTerrorist extends Terrorist {
    private final String realName; // Real identity of the local terrorist
    private final String localCode; // Alias used in communications
    private final String city; // Target city for the attack

    public LocalTerrorist(String realName, String localCode, String city) {
        this.realName = realName;
        this.localCode = localCode;
        this.city = city;
    }

    public String getRealName() {
        return realName;
    }

    public String getLocalCode() {
        return localCode;
    }

    public String getCity() {
        return city;
    }

    // Overrides abstract attack() — local terrorists attack a specific city
    @Override
    public void attack() {
        System.out.println("Attacking city: " + city);
    }

    // Overrides abstract compromise() — returns real name when caught by the agent
    @Override
    public String compromise() {
        return realName;
    }
}

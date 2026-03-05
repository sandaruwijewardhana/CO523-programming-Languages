// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — Terrorist (Abstract Base Class)
//
// Abstraction + Inheritance: Terrorist is an abstract class defining the common
// interface for all terrorist types (LocalTerrorist, GlobalTerrorist).
// attack() and compromise() are abstract — subclasses implement them differently.

public abstract class Terrorist {

    // Buys a weapon from the seller; automatically calls the weapon's deploy() method
    public void buyWeapon(Weapon weapon) {
        weapon.deploy();
    }

    // Abstract method — prints the attack location (city for local, country for global)
    public abstract void attack();

    // Abstract method — returns identifying name (real name or code name)
    public abstract String compromise();
}

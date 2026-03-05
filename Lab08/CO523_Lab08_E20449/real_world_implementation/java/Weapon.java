// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — Weapon (Abstract Base Class)
//
// Abstraction: Weapon is an abstract class defining the common interface
// for all weapon types (Bomb, Missile). Each concrete subclass must
// implement the deploy() method with its own specific behavior.

public abstract class Weapon {
    // Abstract method — must be implemented by each concrete weapon subclass
    public abstract void deploy();
}

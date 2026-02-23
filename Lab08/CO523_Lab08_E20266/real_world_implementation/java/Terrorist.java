public abstract class Terrorist {
    public void buyWeapon(Weapon weapon) {
        weapon.deploy();
    }

    public abstract void attack();

    public abstract String compromise();
}

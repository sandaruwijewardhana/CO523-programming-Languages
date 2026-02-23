public class Seller {
    private static final String PASSWORD = "RAPTOR";
    private final Bomb b1;
    private final Missile m1;

    public Seller() {
        b1 = new Bomb("Clemo", 12.00f);
        m1 = new Missile("0001", "Intercontinental", "nuclear");
    }

    public void sellWeapon(Terrorist terrorist, Agent agent, String password, int weaponChoice) {
        if (!PASSWORD.equals(password)) {
            System.out.println("Access denied. Incorrect password.");
            return;
        }

        if (weaponChoice == 1) {
            System.out.println("Bomb selected: " + b1.getCategory());
            terrorist.buyWeapon(b1);
            terrorist.attack();
            System.out.println("Terrorist escaped after bomb attack.");
        } else if (weaponChoice == 2) {
            System.out.println("Missile selected: " + m1.getCode() + ", " + m1.getRange() + ", " + m1.getType());
            terrorist.buyWeapon(m1);
            agent.catchTerrorist(terrorist);
            agent.promote("Major");
            agent.missionSuccess();
            agent.addExperience();
            System.out.println("Agent record updated after successful capture.");
        } else {
            System.out.println("Invalid weapon selection.");
        }
    }
}

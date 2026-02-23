public class GlobalTerrorist extends Terrorist {
    private final String codeName;
    private final String country;

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

    @Override
    public void attack() {
        System.out.println("Attacking country: " + country);
    }

    @Override
    public String compromise() {
        return codeName;
    }
}

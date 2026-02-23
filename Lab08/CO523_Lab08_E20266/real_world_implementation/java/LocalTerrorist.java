public class LocalTerrorist extends Terrorist {
    private final String realName;
    private final String localCode;
    private final String city;

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

    @Override
    public void attack() {
        System.out.println("Attacking city: " + city);
    }

    @Override
    public String compromise() {
        return realName;
    }
}

public class Missile extends Weapon {
    private final String code;
    private final String range;
    private final String type;

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

    @Override
    public void deploy() {
        System.out.println("Missile ready for launch");
    }
}

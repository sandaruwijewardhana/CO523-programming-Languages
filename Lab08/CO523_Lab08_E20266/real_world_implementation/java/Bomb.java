public class Bomb extends Weapon {
    private final String category;
    private final float duration;

    public Bomb(String category, float duration) {
        this.category = category;
        this.duration = duration;
    }

    public String getCategory() {
        return category;
    }

    public float getDuration() {
        return duration;
    }

    @Override
    public void deploy() {
        System.out.println("Bomb activation time: " + duration + " seconds");
    }
}

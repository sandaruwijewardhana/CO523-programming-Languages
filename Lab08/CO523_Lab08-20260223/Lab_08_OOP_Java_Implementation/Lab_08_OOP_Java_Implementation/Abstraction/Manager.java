class Manager extends Employee {

    @Override
    void work() {
        System.out.println(name + " is managing the team."); // override Abstract method
    }

}

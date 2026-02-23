class Developer extends Employee {

    @Override
    void work() {
        System.out.println(name + " is writing code."); // override Abstract method
    }

}

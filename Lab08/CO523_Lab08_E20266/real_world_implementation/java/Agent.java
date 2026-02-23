public class Agent {
    private final String codeName;
    private final String realName;
    private final int idNumber;
    private final ServiceRecord serviceRecord;

    public Agent(String codeName, String realName, int idNumber, ServiceRecord serviceRecord) {
        this.codeName = codeName;
        this.realName = realName;
        this.idNumber = idNumber;
        this.serviceRecord = serviceRecord;
    }

    public String getCodeName() {
        return codeName;
    }

    public String getRealName() {
        return realName;
    }

    public int getIdNumber() {
        return idNumber;
    }

    public ServiceRecord getServiceRecord() {
        return serviceRecord;
    }

    public void promote(String higherRank) {
        serviceRecord.setPreviousRank(serviceRecord.getCurrentRank());
        serviceRecord.setCurrentRank(higherRank);
    }

    public void missionSuccess() {
        serviceRecord.incrementSuccessfulMissionCount();
    }

    public void addExperience() {
        serviceRecord.incrementYearsOfService();
    }

    public void catchTerrorist(Terrorist terrorist) {
        System.out.println("Terrorist " + terrorist.compromise() + " caught by " + codeName);
    }

    public void printAgentStatus() {
        System.out.println("Agent Real Name: " + realName);
        System.out.println("Agent Code Name: " + codeName);
        System.out.println("ID Number: " + idNumber);
        System.out.println("Previous Rank: " + serviceRecord.getPreviousRank());
        System.out.println("Current Rank: " + serviceRecord.getCurrentRank());
        System.out.println("Years of Service: " + serviceRecord.getYearsOfService());
        System.out.println("Successful Mission Count: " + serviceRecord.getSuccessfulMissionCount());
    }
}

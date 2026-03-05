// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — Agent (Encapsulation + Composition)
//
// Encapsulation: Agent's fields are private and accessed only via getter methods.
// Composition: Agent holds a ServiceRecord object to manage career details.
// The agent can promote, log mission success, gain experience, and catch terrorists.

public class Agent {
    private final String codeName; // Agent's field name (e.g., "007")
    private final String realName; // Agent's actual identity
    private final int idNumber; // Unique agent ID
    private final ServiceRecord serviceRecord; // Composition — agent owns a service record

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

    // Promote method — updates previous rank and assigns a new higher rank
    public void promote(String higherRank) {
        serviceRecord.setPreviousRank(serviceRecord.getCurrentRank());
        serviceRecord.setCurrentRank(higherRank);
    }

    // missionSuccess method — increments successful mission count in the service
    // record
    public void missionSuccess() {
        serviceRecord.incrementSuccessfulMissionCount();
    }

    // addExperience method — increments years of service by one in the service
    // record
    public void addExperience() {
        serviceRecord.incrementYearsOfService();
    }

    // catchTerrorist method — prints a message when the agent apprehends a
    // terrorist
    public void catchTerrorist(Terrorist terrorist) {
        System.out.println("Terrorist " + terrorist.compromise() + " caught by " + codeName);
    }

    // Prints the full status of the agent and their service record
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

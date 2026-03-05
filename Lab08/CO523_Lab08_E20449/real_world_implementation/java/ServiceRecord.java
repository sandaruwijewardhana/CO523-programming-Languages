// CO523 - Programming Languages | Lab 08: Object-Oriented Programming Paradigm
// Section 4.3 Real-world Scenario — ServiceRecord (Encapsulation)
//
// Encapsulation: ServiceRecord stores the agent's career history with private fields.
// All modifications go through controlled methods (setters and increment methods),
// preventing direct external manipulation of the service record data.

public class ServiceRecord {
    private String previousRank; // Rank before the most recent promotion
    private String currentRank; // Agent's current active rank
    private int yearsOfService; // Total years the agent has served
    private int successfulMissionCount; // Number of missions completed successfully

    public ServiceRecord(String previousRank, String currentRank, int yearsOfService, int successfulMissionCount) {
        this.previousRank = previousRank;
        this.currentRank = currentRank;
        this.yearsOfService = yearsOfService;
        this.successfulMissionCount = successfulMissionCount;
    }

    public String getPreviousRank() {
        return previousRank;
    }

    public void setPreviousRank(String previousRank) {
        this.previousRank = previousRank;
    }

    public String getCurrentRank() {
        return currentRank;
    }

    public void setCurrentRank(String currentRank) {
        this.currentRank = currentRank;
    }

    public int getYearsOfService() {
        return yearsOfService;
    }

    public int getSuccessfulMissionCount() {
        return successfulMissionCount;
    }

    // Increments years of service by one (called via Agent.addExperience())
    public void incrementYearsOfService() {
        yearsOfService++;
    }

    // Increments successful mission count by one (called via
    // Agent.missionSuccess())
    public void incrementSuccessfulMissionCount() {
        successfulMissionCount++;
    }
}

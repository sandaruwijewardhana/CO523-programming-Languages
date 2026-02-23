public class ServiceRecord {
    private String previousRank;
    private String currentRank;
    private int yearsOfService;
    private int successfulMissionCount;

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

    public void incrementYearsOfService() {
        yearsOfService++;
    }

    public void incrementSuccessfulMissionCount() {
        successfulMissionCount++;
    }
}

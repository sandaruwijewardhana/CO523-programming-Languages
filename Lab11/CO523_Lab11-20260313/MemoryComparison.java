class DataObject {
    String type;

    DataObject(String type) {
        this.type = type;
        System.out.println("Heap: DataObject (" + type + ") allocated in memory.");
    }

    @Override
    protected void finalize() {
        System.out.println("Heap: DataObject (" + type + ") is being reclaimed.");
    }
}

public class MemoryComparison {
    public static void main(String[] args) {
        System.out.println("--- Entering main method (Stack Frame created) ---");
        processData();
        System.out.println("--- Returned to main method ---");
        
        // Suggesting GC to see the heap object cleanup
        System.gc();
    }

    static void processData() {
        System.out.println("--- Entering processData() ---");

        // 1. Stack Variable: Local primitive
        int stackValue = 100;
        System.out.println("Stack: local variable 'stackValue' (" + stackValue + ") created.");

        // 2. Heap Object: Created inside the function
        DataObject heapObj = new DataObject("DynamicData"); 
        
        System.out.println("--- Exiting processData() ---");
    } // stackValue and the reference heapObj are destroyed here 
}
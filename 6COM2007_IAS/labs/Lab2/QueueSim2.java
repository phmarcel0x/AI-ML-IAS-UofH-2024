import java.util.LinkedList;
import java.util.Random;

public class QueueSim2 {

    private static final int SIMULATION_TIME = 100; // Simulation duration in seconds
    private static final int ARRIVAL_RATE = 1; // Customers arriving per second
    private static final int SERVICE_TIME = 1; // Service time per customer (seconds)

    // Data structures
    private LinkedList<Integer> queue = new LinkedList<>(); // Queue to hold customers
    private int serverBusyUntil = 0; // Time when server becomes free (0 if idle)
    private int currentTime = 0; // Current simulation time

    public static void main(String[] args) {
        QueueSim2 simulation = new QueueSim2();
        simulation.runSimulation();
    }

    public void runSimulation() {
        Random random = new Random();

        while (currentTime < SIMULATION_TIME) {
            // Check for customer arrival
            if (random.nextDouble() < ARRIVAL_RATE * (0.1)) { // Check every 0.1 seconds
                queue.add(currentTime); // Add arrival time to queue
            }

            // Check if server becomes free
            if (serverBusyUntil > 0 && currentTime >= serverBusyUntil) {
                serverBusyUntil = 0; // Server becomes free
            }

            // Serve a customer if server is free and queue is not empty
            if (serverBusyUntil == 0 && !queue.isEmpty()) {
                serverBusyUntil = currentTime + SERVICE_TIME; // Update server busy state
				
            }

            // Update time
            currentTime++;

            // Print statistics
            System.out.println("Time: " + currentTime + ", Queue size: " + queue.size() + ", Server busy: " + serverBusyUntil);
        }

        // Calculate and print average queue length
        double averageQueueLength = 0;
        for (int time : queue) {
			System.out.println("queue " + queue);
            averageQueueLength = averageQueueLength+ currentTime - time;
        }
        averageQueueLength = averageQueueLength/queue.size(); 
        System.out.println("Average queue length: " + averageQueueLength);
    }
}
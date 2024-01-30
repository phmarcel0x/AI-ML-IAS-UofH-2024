import java.util.Scanner;
//import org.jfree.chart;

public class Greenhouse {
    public static void main(String[] args) {
        //Scanner input = new Scanner(System.in);

        double desiredTemp = 75.0; // Target temperature
        double currentTemp = 70.0; // Initial temperature
        double adjustmentFactorTemp = 0.1; // Temperature adjustment rate
        
        double desiredMoisture = 60.0; // Target moisture level
        double currentMoisture = 55.0; // Initial moisture level
        double adjustmentFactorMoisture = 0.2; // Moisture adjustment rate

        double plantGrowthRate = 0.05; // Plant growth rate based on temperature and moisture

        System.out.println("Initial state:");
        System.out.println("Temperature: " + currentTemp);
        System.out.println("Moisture: " + currentMoisture);

        while (true) {
            // Negative feedback loop for temperature
            double tempDifference = desiredTemp - currentTemp;
            currentTemp += adjustmentFactorTemp * tempDifference;
            // Positive feedback loop for plant growth
            double growthFactor = currentTemp * currentMoisture * plantGrowthRate;
            // Negative feedback loop for moisture (adjusted by plant growth)
            double moistureDifference = desiredMoisture - (currentMoisture +
            growthFactor);
            currentMoisture += adjustmentFactorMoisture * moistureDifference;
            System.out.println("\nCurrent state:");
            System.out.println("Temperature: " + currentTemp);
            System.out.println("Moisture: " + currentMoisture);
            System.out.println("Plant growth: " + growthFactor);
            // Simulate external factors
            currentTemp += (Math.random() - 0.5) * 2; // Random temperature fluctuations
            currentMoisture -= (Math.random() - 0.5) * 1; // Random moisture fluctuations

            // Check for stability (optional)
            if (Math.abs(tempDifference) < 0.1 && Math.abs(moistureDifference) < 0.2) {
            System.out.println("\nStable environment achieved.");
            break;
        }
    }
}
}
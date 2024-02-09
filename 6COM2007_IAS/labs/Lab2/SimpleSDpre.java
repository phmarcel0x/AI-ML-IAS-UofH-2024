/*
 * SimpleSDpre.java
 * An example of a system dynamics model implemented in Java
 */

 import java.util.Scanner;
import java.io.PrintWriter;
import java.io.IOException;

public class SimpleSDpre {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Initial system variables
        double population = 10000;  // Initial population
        double birthRate = 0.025;  // Annual birth rate
        double deathRate = 0.015;  // Base annual death rate
        double congestion = 1;

        // Simulation loop
        int numYears = 500;
        try {
            PrintWriter writer = new PrintWriter("output.csv", "UTF-8");
            writer.println("Year,Population,Death Rate");  // Write the header
            for (int year = 1; year <= numYears; year++) {

                // Update congestion based on current population
                congestion = population / 10000;
                deathRate *= congestion;

                // Calculate population change
                double births = birthRate * population;
                double deaths = deathRate * population;

                double netChange = births - deaths;

                // Update population
                population += netChange;

                // Write results to the CSV file
                writer.println(year + "," + String.format("%.2f", population) + "," + String.format("%.5f", deathRate));
            }
            writer.close();
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
        scanner.close();
    }
}
package SimpleSDpreRandomSolution;
/*
 * SimpleSDpre.java
 * An example of a system dynamics model implemented in Java (with random initial values)
 */

 import java.util.Scanner;
 import java.io.PrintWriter;
 import java.io.IOException;
 
 class Region {
     double population;
     double birthRate;
     double deathRate;
     double congestion;
 
     public Region() {
         // Random initial system variables
         this.population = 10000 + (int)(Math.random() * 10000);  // Random initial population
         this.birthRate = 0.025 + (Math.random() * 0.025);  // Random initial birth rate
         this.deathRate = 0.015 + (Math.random() * 0.015);  // Random initial death rate
         this.congestion = 1 + (Math.random() * 1);  // Random initial congestion
     }
 
     public void simulateYear() {
         // Update congestion based on current population
         congestion = population / 10000;
         deathRate *= congestion;
 
         // Calculate population change randomly
         double births = birthRate * population;
         double deaths = deathRate * population;
 
         // Add random noise to the net change
         double netChange = births - deaths + (Math.random() * 1000 - 500);  // Random noise between -500 and 500
 
         // Update population
         population += netChange;
     }
 
     public void migrate(Region other, double rate) {
         double migrants = this.population * rate;
         this.population -= migrants;
         other.population += migrants;
     }
 }
 
 public class SimpleSDpre_Random {
     public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);
 
         // Create regions with random initial system variables
         Region region1 = new Region();
         Region region2 = new Region();
 
         // Simulation loop
         int numYears = 500;
         try {
             PrintWriter writer = new PrintWriter("outputRandom.csv", "UTF-8");
             writer.println("Year,Region1 Population,Region2 Population");  // Write the header
             for (int year = 1; year <= numYears; year++) {
                 // Simulate year for each region
                 region1.simulateYear();
                 region2.simulateYear();
 
                 // Simulate migration between regions
                 region1.migrate(region2, 0.01);  // 1% of population migrates from region1 to region2
                 region2.migrate(region1, 0.01);  // 1% of population migrates from region2 to region1
 
                 // Write results to the CSV file
                 writer.println(year + "," + String.format("%.2f", region1.population) + "," + String.format("%.2f", region2.population));
             }
             writer.close();
         } catch (IOException e) {
             System.out.println("An error occurred while writing to the file.");
             e.printStackTrace();
         }
         scanner.close();
     }
 }
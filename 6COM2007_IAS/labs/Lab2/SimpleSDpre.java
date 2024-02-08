/*
 * SimpleSDpre.java
 * An example of a system dynamics model implemented in Java
 */

 import java.util.Scanner;

 public class SimpleSDpre {
     public static void main(String[] args) {
         Scanner scanner = new Scanner(System.in);
 
         // Initial system variables
         double population = 10000;  // Initial population
         double birthRate = 0.025;  // Annual birth rate
         double deathRate = 0.015;  // Base annual death rate
         double congestion = 1;
         double adjustedDeathRate = deathRate * congestion;
 
         // Simulation loop
         int numYears = 50;
         for (int year = 1; year <= numYears; year++) {
             // Calculate population change
             double births = birthRate * population;
             double deaths = adjustedDeathRate * population; 
            
             // Update congestion based on current population
             congestion = population / 10000;
             
             double netChange = births - deaths;
 
             // Update population
             population = population + netChange;
 
             // Print results
             System.out.println("Year " + year + ": Population = " + String.format("%.2f", population) + ", Death Rate = " + String.format("%.5f", adjustedDeathRate));
         }
         scanner.close();
     }
 }
 

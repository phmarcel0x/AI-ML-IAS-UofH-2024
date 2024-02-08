import java.util.ArrayList;
import java.util.List;

class Agent {

    // Agent properties
    private int x, y;  // Position coordinates

    // Agent behavior
    public void move() {
        // Implement movement logic here, e.g., random walk or goal-seeking
        x += (int) (Math.random() * 5) - 2;  // Random movement example
        y += (int) (Math.random() * 5) - 2;
		System.out.println("agent = "+ x);
		System.out.println("x = "+ x);
		System.out.println("y = "+ y);
		
    }

    // Insert additional methods for interacting with other agents or the environment

}

public class AgentBasedSimulation {

    public static void main(String[] args) {
        List<Agent> agents = new ArrayList<>();

        // Create agents and initialise their properties
        for (int i = 0; i < 10; i++) {
            Agent agent = new Agent();
            // Set initial positions or other properties
            agents.add(agent);
			
			System.out.println(i + " agents" );
        }

        // Simulation loop
        for (int step = 0; step < 100; step++) {
            for (Agent agent : agents) {
                agent.move();  // Allow each agent to act
                // Implement any interactions or updates based on agents' actions
				System.out.println(step + " steps");
            }
            // analyze the agents' state (todo)
			System.out.println();
			//visualise
        }
    }
}

import java.util.ArrayList;
import java.util.List;

class Agent {
    // Agent properties
    private int x, y;  // Position coordinates

    public int getX() { return x; }
    public int getY() { return y; }

    // Agent behavior
    public void move() {
        // Implement movement logic here, e.g., random walk or goal-seeking
        x += (int) (Math.random() * 5) - 2;  // Random movement example
        y += (int) (Math.random() * 5) - 2;
    }
}

public class AgentBasedSimulation {
    public static void main(String[] args) {
        List<Agent> agents = new ArrayList<>();

        // Create agents and initialise their properties
        for (int i = 0; i < 10; i++) {
            Agent agent = new Agent();
            agents.add(agent);
        }

        // Simulation loop
        for (int step = 0; step < 100; step++) {
            for (Agent agent : agents) {
                agent.move();  // Allow each agent to act
            }

            // Visualize
            for (int y = 0; y < 20; y++) {
                for (int x = 0; x < 20; x++) {
                    boolean hasAgent = false;
                    for (Agent agent : agents) {
                        if (agent.getX() == x && agent.getY() == y) {
                            hasAgent = true;
                            break;
                        }
                    }
                    System.out.print(hasAgent ? "A" : ".");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
}
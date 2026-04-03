import numpy as np
import matplotlib.pyplot as plt

def simulate(num_cars):
    road_length = 100
    max_speed = 2
    safe_distance = 5

    positions = np.linspace(0, road_length, num_cars, endpoint=False)
    velocities = np.ones(num_cars) * max_speed

    for step in range(200):
        new_velocities = velocities.copy()

        for i in range(num_cars):
            next_car = (i + 1) % num_cars
            distance = (positions[next_car] - positions[i]) % road_length

            if distance < safe_distance:
                new_velocities[i] = max(0, velocities[i] - 0.3)
            else:
                new_velocities[i] = min(max_speed, velocities[i] + 0.1)

        velocities = new_velocities
        positions = (positions + velocities) % road_length

    return np.mean(velocities)

# Run experiments
car_counts = range(5, 60, 5)
avg_speeds = [simulate(n) for n in car_counts]

# Compute flow
flow = [n * v for n, v in zip(car_counts, avg_speeds)]

# Plot graph
plt.plot(car_counts, flow)
plt.xlabel("Density (Number of Cars)")
plt.ylabel("Flow (Density × Speed)")
plt.title("Fundamental Diagram of Traffic Flow")

# Save image
plt.savefig("traffic_flow.png")

plt.show()
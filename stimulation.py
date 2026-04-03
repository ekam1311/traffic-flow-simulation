import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_cars = 5
road_length = 100
max_speed = 2
safe_distance = 5

# Initial state
positions = np.linspace(0, road_length, num_cars, endpoint=False)
velocities = np.ones(num_cars) * max_speed

# Plot setup
fig, ax = plt.subplots()
scat = ax.scatter(positions, np.zeros(num_cars), s=50)

ax.set_xlim(0, road_length)
ax.set_ylim(-1, 1)
ax.set_title("Traffic Flow Simulation (Shockwave Behavior)")

def update(frame):
    global positions, velocities

    new_velocities = velocities.copy()

    for i in range(num_cars):
        next_car = (i + 1) % num_cars
        distance = (positions[next_car] - positions[i]) % road_length

        # Random braking → creates shockwaves
        if np.random.rand() < 0.05:
            new_velocities[i] = max(0, velocities[i] - 1)

        elif distance < safe_distance:
            new_velocities[i] = max(0, velocities[i] - 0.5)
        else:
            new_velocities[i] = min(max_speed, velocities[i] + 0.2)

    velocities[:] = new_velocities
    positions[:] = (positions + velocities) % road_length

    scat.set_offsets(np.c_[positions, np.zeros(num_cars)])
    return scat,

ani = animation.FuncAnimation(
    fig, update, frames=200, interval=50, blit=True
)

plt.show()
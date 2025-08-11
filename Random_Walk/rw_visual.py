import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Keep making new walks, as long as the program  is active.

while True:
    #Make a random walk
    rw = RandomWalk(50)
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_value, rw.y_value, linewidth=1)
    ax.set_aspect('equal')

    #Emphasize the first and last points.
    ax.plot(0, 0, linewidth=3)
    ax.plot(rw.x_value[-1], rw.y_value[-1], linewidth=3)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
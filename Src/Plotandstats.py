import matplotlib as plt
import numpy as np

import pandas as pd

from matplotlib.pyplot import xlabel, ylabel

def plot_party_performance(parties):
    if not parties:
        print("No party data available to plot.")
        return

    # Extract names and total seats from the parties
    names = [party.name for party in parties.values()]  # Use .values() to get party objects
    total_seats = [party.total_seats for party in parties.values()]  # Corrected variable name

    # Set x and y labels
    plt.xlabel('Parties')
    plt.ylabel('Seats Won')

    # Plotting
    plt.bar(names, total_seats, color='skyblue')  # Use plt.bar for bar chart
    plt.title('Party Performance for June 2024')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def save_statistics(parties):
    try:
        with open("statistics.txt", "w") as file:
            for party in parties.values():
                file.write(str(party) + "\n")
            print("Statistics saved to 'statistics.txt'.")
    except IOError as e:
        print(f"Error saving statistics: {e}")

# Example usage (assuming you have a Party class and a list of party objects)
# parties = {
#     'Party A': Party('Party A', 10),
#     'Party B': Party('Party B', 15),
#     'Party C': Party('Party C', 5)
# }
# plot_party_performance(parties)
# save_statistics(parties)
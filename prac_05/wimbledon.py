"""
wimbledon_champions.py
Estimate: 20 minutes
"""


def read_data(filename):
    """Reads data from a CSV file and returns a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        return [line.strip().split(',') for line in in_file.readlines()[1:]]


def count_champions(data):
    """Counts the number of wins for each champion."""
    champion_counts = {}
    for row in data:
        champion = row[2].strip()
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
    return champion_counts


def get_unique_countries(data):
    """Gets unique countries of the champions."""
    countries = {row[1].strip() for row in data}
    return countries


def main():
    """Main function to run the program."""
    data = read_data("wimbledon_data.csv")  # Adjust filename if needed
    champion_counts = count_champions(data)
    unique_countries = get_unique_countries(data)

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_counts.items()):
        print(f"{champion} {count}")

    print("\nThese countries have won Wimbledon:")
    print(", ".join(sorted(unique_countries)))


if __name__ == "__main__":
    main()

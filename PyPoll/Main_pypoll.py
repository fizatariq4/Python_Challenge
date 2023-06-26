import csv

# Set the path to the CSV file
file_path = "election_data.csv"

# Initialize variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, "r") as file:
    csvreader = csv.reader(file, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Iterate over the rows in the CSV file
    for row in csvreader:
        # Count the total number of votes cast
        total_votes += 1

        # Retrieve the candidate from the current row
        candidate = row[2]

        # If the candidate is not in the dictionary, add them and initialize their vote count
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        # Increment the vote count for the candidate
        candidate_votes[candidate] += 1

# Print the analysis results
print("Election Results")
print("--------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")

# Iterate over the candidate votes dictionary
for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes each candidate won
    vote_percentage = (votes / total_votes) * 100

    # Print the candidate, their vote percentage, and the total number of votes they won
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

    # Check if the candidate has more votes than the current winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------")
print(f"Winner: {winner}")
print("-------------------")


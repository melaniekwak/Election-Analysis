#The data we need to retrieve.
import csv
import os
#file_outpath = os.path.join("..", "output", "election_results.csv")
file_to_load = 'election_results.csv'
file_to_save = os.path.join("..", "analysis", "election-analysis.txt")

os.chdir("/Users/melaniekwak/Desktop/Election-Analysis/resources")
path = os.getcwd
#print(path)
election_data = open(file_to_load, 'r')
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)

election_data.close()

file_to_save = os.path.join("..", "analysis", "election-analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n\nArapahoe\nDenver\nJefferson")
#file_to_save.close()

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
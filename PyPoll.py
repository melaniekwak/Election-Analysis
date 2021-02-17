#The data we need to retrieve.
import csv
import os
#file_outpath = os.path.join("..", "output", "election_results.csv")
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election-analysis.txt")

election_data = open(file_to_load, 'r')
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

county_options = []
county_votes = {}
#county with largest turnout & number of votes of that county
county_turnout = ""
county_count = 0
largest_county_votes = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
    
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for county_name in county_votes:
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        if (votes > county_count):
            county_count = votes
            county_turnout = county_votes
        print(f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")   
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")   
        txt_file.write(county_results)

        if (votes > largest_county_votes):
            largest_county_votes = votes
            largest_county = county_name 

    county_turnout_summary = (
        f"--------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"--------------------------\n")
    print(county_turnout_summary)
    txt_file.write(county_turnout_summary)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

election_data.close()

file_to_save = os.path.join("..", "analysis", "election-analysis.txt")
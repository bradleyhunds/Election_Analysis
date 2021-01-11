# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# %%

# Open the election results and read the file.
election_data = open(file_to_load, 'r')
# %%
# To do: perform analysis

# Close the file.
election_data.close()
# %%

# Open the election results and read the file
with open(file_to_load) as election_data: 

    # To do: perform analysis.
    print(election_data)
# %%





import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)
# %%

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election analysis.txt")

# Using the open() function with the "w" mode we will write data to the file
open(file_to_save,"w")
# %%

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the with statement open the file as a test file.
outfile = open(file_to_save,"w")

# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
# %%



# Create a filename variable to a dirvet or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")
# %%







# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0 

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
Winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
         #  Add to the total vote count.
         total_votes += 1
         # Print the candidate name from each row.
         candidate_name = row[2]

         if candidate_name not in candidate_options:           
             # Add it to the list of candidates.
             candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
             candidate_votes[candidate_name] = 0
             # Add a vote to that candidate's count.
             candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
                f"\nElection Results\n"
                f"----------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"----------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        for candidate_name in candidate_votes:
            # Retrieve the vote count of a candidate.
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100 
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 

         # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to the file
        txt_file.write(candidate_results)


        if (votes > winning_count) and (vote_percentage > winning_percentage):       
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
                

        print(winning_candidate_summary) 


        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)
# %%




















































            # Save the results to our text file.
            with open(file_to_save, "w") as text_file:

            # Print the final vote count to the terminal.
            election_results = (
                f"\nElection Results\n"
                f"----------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"----------------------------\n")

            print(election_results, end="")

            # Save the final vote count to the text file.
            txt_file.write(election_results)
            # %%
            #  Iterate through the candidate list
            for candidate_name in candidate_votes:
                #  Retrieve the vote count of a candidate.
                votes = candidate_votes[candidate_name]
                #  Calculate the percentage of votes.
                vote_percentage = float(votes) / float(total_votes) * 100

                
                # To do: print out the winning candidate, vote count and percentage to the terminal
                print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
                
                # Determine the winning vote count and candidate
                # Determine if the votes are greater than the winning count.

                if (votes > winning_count) and (vote_percentage > winning_percentage):       
                    winning_count = votes
                    winning_percentage = vote_percentage
                    winning_candidate = candidate_name

            winning_candidate_summary = (
                f"--------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"--------------------------\n")
            print(winning_candidate_summary)
            # %%
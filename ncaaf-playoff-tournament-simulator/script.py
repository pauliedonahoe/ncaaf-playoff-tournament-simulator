#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Description - The below code does the following:
### 1 - inputs a CSV file containing twelve NCAAF teams, their seed for the tournament (#1 through #12), and their 
###     Predictive Rating from TeamRankings.com
### 2 - runs a defined number of simulations (using number_of_simulations input variable) of the NCAAF playoff format
###     using these twelve teams
### 3 - outputs the percentage probability (out of 100) for each team to win in each round of the playoff

## Import packages
import pandas as pd
from collections import Counter
import numpy as np

## Inputs
input_csv_file_path = '/YOUR_FILE_PATH/tournament_data.csv'
number_of_simulations = 10000

## No output files - only outputs in console


# In[4]:


# Read the CSV file
df = pd.read_csv(input_csv_file_path)  # Replace with your file path

# Dictionary to map numeric seeds to text
seed_names = {
    1: "one_seed",
    2: "two_seed",
    3: "three_seed",
    4: "four_seed",
    5: "five_seed",
    6: "six_seed",
    7: "seven_seed",
    8: "eight_seed",
    9: "nine_seed",
    10: "ten_seed",
    11: "eleven_seed",
    12: "twelve_seed",
}

# Assign each row to a variable named after the seed
for _, row in df.iterrows():
    seed = int(row['Seed'])
    var_name = seed_names.get(seed, f"seed_{seed}_unknown")
    globals()[var_name] = row

# Example: Access the one_seed variable
print(one_seed)


# In[5]:


# Archive lists to store all the results across runs
archive_round_of_twelve_winners = []
archive_elite_eight_winners = []
archive_final_four_winners = []
archive_championship_winner = []

# Run the simulation 10,000 times
for _ in range(number_of_simulations):
    round_of_twelve_winners = []

    # 12 seed @ 5 seed
    while True:
        random_value_five_v_twelve = np.random.normal(
            loc=(five_seed['Rating'] - twelve_seed['Rating']) + 2.6,
            scale=13.89
        )
        if random_value_five_v_twelve < -0.5 or random_value_five_v_twelve > 0.5:
            break

    if random_value_five_v_twelve > 0:
        round_of_twelve_winners.append(five_seed)
        elite_eight_five = five_seed
    else:
        round_of_twelve_winners.append(twelve_seed)
        elite_eight_five = twelve_seed

    # 11 seed @ 6 seed
    while True:
        random_value_six_v_eleven = np.random.normal(
            loc=(six_seed['Rating'] - eleven_seed['Rating']) + 2.6,
            scale=13.89
        )
        if random_value_six_v_eleven < -0.5 or random_value_six_v_eleven > 0.5:
            break

    if random_value_six_v_eleven > 0:
        round_of_twelve_winners.append(six_seed)
        elite_eight_six = six_seed
    else:
        round_of_twelve_winners.append(eleven_seed)
        elite_eight_six = eleven_seed

    # 7 seed @ 10 seed
    while True:
        random_value_seven_v_ten = np.random.normal(
            loc=(seven_seed['Rating'] - ten_seed['Rating']) + 2.6,
            scale=13.89
        )
        if random_value_seven_v_ten < -0.5 or random_value_seven_v_ten > 0.5:
            break

    if random_value_seven_v_ten > 0:
        round_of_twelve_winners.append(seven_seed)
        elite_eight_seven = seven_seed
    else:
        round_of_twelve_winners.append(ten_seed)
        elite_eight_seven = ten_seed

    # 8 seed @ 9 seed
    while True:
        random_value_eight_v_nine = np.random.normal(
            loc=(eight_seed['Rating'] - nine_seed['Rating']) + 2.6,
            scale=13.89
        )
        if random_value_eight_v_nine < -0.5 or random_value_eight_v_nine > 0.5:
            break

    if random_value_eight_v_nine > 0:
        round_of_twelve_winners.append(eight_seed)
        elite_eight_eight = eight_seed
    else:
        round_of_twelve_winners.append(nine_seed)
        elite_eight_eight = nine_seed

    # Elite Eight
    elite_eight_winners = []

    # 1 seed vs. 8/9 winner
    while True:
        random_value__elite_eight_one = np.random.normal(
            loc=(one_seed['Rating'] - elite_eight_eight['Rating']),
            scale=13.89
        )
        if random_value__elite_eight_one < -0.5 or random_value__elite_eight_one > 0.5:
            break

    if random_value__elite_eight_one > 0:
        elite_eight_winners.append(one_seed)
        final_four_one = one_seed
    else:
        elite_eight_winners.append(elite_eight_eight)
        final_four_one = elite_eight_eight

    # 2 seed vs. 7/10 winner
    while True:
        random_value_two_v_seven = np.random.normal(
            loc=(two_seed['Rating'] - elite_eight_seven['Rating']),
            scale=13.89
        )
        if random_value_two_v_seven < -0.5 or random_value_two_v_seven > 0.5:
            break

    if random_value_two_v_seven > 0:
        elite_eight_winners.append(two_seed)
        final_four_two = two_seed
    else:
        elite_eight_winners.append(elite_eight_seven)
        final_four_two = elite_eight_seven

    # 3 seed vs. 6/11 winner
    while True:
        random_value_three_v_six = np.random.normal(
            loc=(three_seed['Rating'] - elite_eight_six['Rating']),
            scale=13.89
        )
        if random_value_three_v_six < -0.5 or random_value_three_v_six > 0.5:
            break

    if random_value_three_v_six > 0:
        elite_eight_winners.append(three_seed)
        final_four_three = three_seed
    else:
        elite_eight_winners.append(elite_eight_six)
        final_four_three = elite_eight_six

    # 4 seed vs. 5/12 winner
    while True:
        random_value_four_v_five = np.random.normal(
            loc=(four_seed['Rating'] - elite_eight_five['Rating']),
            scale=13.89
        )
        if random_value_four_v_five < -0.5 or random_value_four_v_five > 0.5:
            break

    if random_value_four_v_five > 0:
        elite_eight_winners.append(four_seed)
        final_four_four = four_seed
    else:
        elite_eight_winners.append(elite_eight_five)
        final_four_four = elite_eight_five

    # Final Four
    final_four_winners = []

    # 1/8/9 winner vs. 4/5/12 winner
    while True:
        random_value__final_four_one = np.random.normal(
            loc=(final_four_one['Rating'] - final_four_four['Rating']),
            scale=13.89
        )
        if random_value__final_four_one < -0.5 or random_value__final_four_one > 0.5:
            break

    if random_value__final_four_one > 0:
        final_four_winners.append(final_four_one)
        championship_one = final_four_one
    else:
        final_four_winners.append(final_four_four)
        championship_one = final_four_four

    # 2/7/10 winner vs. 3/6/11 winner
    while True:
        random_value__final_four_two = np.random.normal(
            loc=(final_four_two['Rating'] - final_four_three['Rating']),
            scale=13.89
        )
        if random_value__final_four_two < -0.5 or random_value__final_four_two > 0.5:
            break

    if random_value__final_four_two > 0:
        final_four_winners.append(final_four_two)
        championship_two = final_four_two
    else:
        final_four_winners.append(final_four_three)
        championship_two = final_four_three

    # National Championship
    championship_winner = []

    while True:
        random_value__championship = np.random.normal(
            loc=(championship_one['Rating'] - championship_two['Rating']),
            scale=13.89
        )
        if random_value__championship < -0.5 or random_value__championship > 0.0:
            break

    if random_value__championship > 0:
        championship_winner.append(championship_one)
        national_champion = championship_one
    else:
        championship_winner.append(championship_two)
        national_champion = championship_two

    # Archive results
    archive_round_of_twelve_winners.extend(round_of_twelve_winners)
    archive_elite_eight_winners.extend(elite_eight_winners)
    archive_final_four_winners.extend(final_four_winners)
    archive_championship_winner.extend(championship_winner)

# Round of twelve - results

# Count occurrences of each Team
team_counts = Counter(item["Team"] for item in archive_round_of_twelve_winners)

# Calculate percentage = (count / 10000) * 100
team_percentages = {team: (count / 10000) * 100 for team, count in team_counts.items()}

# Convert to DataFrame for a nice tabular output
df = pd.DataFrame([
    {"Team": team, "Percentage": percentage}
    for team, percentage in team_percentages.items()
])

# Sort descending by Percentage
df = df.sort_values(by='Percentage', ascending=False)

print("Round of twelve percentages:")

print(df.to_string(index=False))

# Elite eight - results

# Count occurrences of each Team
team_counts = Counter(item["Team"] for item in archive_elite_eight_winners)

# Calculate percentage = (count / 10000) * 100
team_percentages = {team: (count / 10000) * 100 for team, count in team_counts.items()}

# Convert to DataFrame for a nice tabular output
df = pd.DataFrame([
    {"Team": team, "Percentage": percentage}
    for team, percentage in team_percentages.items()
])

# Sort descending by Percentage
df = df.sort_values(by='Percentage', ascending=False)

print("Elite eight percentages:")

print(df.to_string(index=False))

# Final four - results

# Count occurrences of each Team
team_counts = Counter(item["Team"] for item in archive_final_four_winners)

# Calculate percentage = (count / 10000) * 100
team_percentages = {team: (count / 10000) * 100 for team, count in team_counts.items()}

# Convert to DataFrame for a nice tabular output
df = pd.DataFrame([
    {"Team": team, "Percentage": percentage}
    for team, percentage in team_percentages.items()
])

# Sort descending by Percentage
df = df.sort_values(by='Percentage', ascending=False)

print("Final four percentages:")

print(df.to_string(index=False))

# National championship - results

# Count occurrences of each Team
team_counts = Counter(item["Team"] for item in archive_championship_winner)

# Calculate percentage = (count / 10000) * 100
team_percentages = {team: (count / 10000) * 100 for team, count in team_counts.items()}

# Convert to DataFrame for a nice tabular output
df = pd.DataFrame([
    {"Team": team, "Percentage": percentage}
    for team, percentage in team_percentages.items()
])

# Sort descending by Percentage
df = df.sort_values(by='Percentage', ascending=False)

print("National champion percentages:")

print(df.to_string(index=False))


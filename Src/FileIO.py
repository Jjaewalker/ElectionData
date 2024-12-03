import csv
import Classes

# Dictionaries to store data
parties = {}
constituencies = {}
mps = []

def read_election_data(filename):
    try:
        #Read data from CSV file
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                process_row(row)

    except FileNotFoundError:
        print(f"File not found: {filename}")

def process_row(row):
    # Extract data from the row
    constituency_name = row['Constituency']
    nation = row['Nation']
    party_name = row['Party']
    votes_received = int(row['Votes Received'])
    gender = row['Gender']
    # THIS IS AN EXAMPLE ^^^^

    # Create or get Constituency object
    if constituency_name not in constituencies:
        constituency = Classes.Constituency(constituency_name, registered_voters, total_votes_cast, nation)
        constituencies[constituency_name] = constituency
    else:
        constituency = constituencies[constituency_name]

    # Create or get Party object
    if party_name not in parties:
        party = Party(party_name)
        parties[party_name] = party
    else:
        party = parties[party_name]

    # Create MP object
    mp = MP(candidate_name, party_name, constituency_name, votes_received, gender)
    mps.append(mp)

    # Add MP to constituency and party
    constituency.add_candidate(mp)
    party.add_mp(mp)

# Total votes per party
def load_data(file_path):
    constituencies = {}
    parties = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Constituency data
                constituency_name = row["Constituency"]
                nation = row["Nation"]
                registered_voters = int(row["Registered Voters"])
                votes_cast = int(row["Votes Cast"])
                if constituency_name not in constituencies:
                    constituencies[constituency_name] = Constituency(
                        constituency_name, nation, registered_voters, votes_cast
                    )

                # Candidate data
                name = row["Candidate Name"]
                party = row["Party"]
                votes = int(row["Votes"])
                percentage = float(row["Percentage"])
                candidate = mp(name, party, constituency_name, votes, percentage)

                # Add candidate to constituency
                constituencies[constituency_name].add_candidate(candidate)

                # Party data
                if party not in parties:
                    parties[party] = party(party)
                parties[party].add_votes(votes)
                if votes == max(v["Votes"] for v in constituencies[constituency_name].candidates):
                    parties[party].add_seat()

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return constituencies, parties
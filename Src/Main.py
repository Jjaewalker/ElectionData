


# Class Definitions
class MP:
    def __init__(self, name, party, constituency, votes_received, gender):
        self.name = name
        self.party = party
        self.constituency = constituency
        self.votes_received = votes_received
        self.gender = gender

class Party:
    def __init__(self, name):
        self.name = name
        self.total_votes = 0
        self.number_of_mps = 0
        self.male_mps = 0
        self.female_mps = 0

    def add_mp(self, mp):
        self.number_of_mps += 1
        self.total_votes += mp.votes_received
        if mp.gender.lower() == 'male':
            self.male_mps += 1
        elif mp.gender.lower() == 'female':
            self.female_mps += 1

    def get_gender_percentage(self):
        total = self.male_mps + self.female_mps
        if total > 0:
            male_percent = (self.male_mps / total) * 100
            female_percent = (self.female_mps / total) * 100
            return {'male': male_percent, 'female': female_percent}
        else:
            return {'male': 0, 'female': 0}

class Constituency:
    def __init__(self, name, registered_voters, total_votes_cast, nation):
        self.name = name
        self.registered_voters = registered_voters
        self.total_votes_cast = total_votes_cast
        self.nation = nation
        self.candidates = []
        self.elected_mp = None

    def add_candidate(self, mp):
        self.candidates.append(mp)
        # Determine if this candidate is the elected MP
        if (not self.elected_mp) or (mp.votes_received > self.elected_mp.votes_received):
            self.elected_mp = mp

    def turnout_percentage(self):
        if self.registered_voters > 0:
            return (self.total_votes_cast / self.registered_voters) * 100
        else:
            return 0

# Dictionaries to store data
parties = {}
constituencies = {}
mps = []

def read_election_data(filename):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == '.csv':
        # Read data from CSV file
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                process_row(row)
    elif file_extension == '.xlsx':
        # Read data from Excel file using pandas
        df = pd.read_excel(filename)
        # Convert DataFrame rows to dictionaries
        for index, row in df.iterrows():
            # Convert row to a dictionary with string keys
            row_dict = row.to_dict()
            row_dict = {str(k): v for k, v in row_dict.items()}
            process_row(row_dict)
    else:
        print(f"Unsupported file type: {file_extension}")

def process_row(row):
    # Extract data from the row
    constituency_name = row['Constituency']
    nation = row['Nation']
    registered_voters = int(row['Registered Voters'])
    total_votes_cast = int(row['Total Votes Cast'])
    candidate_name = row['Candidate Name']
    party_name = row['Party']
    votes_received = int(row['Votes Received'])
    gender = row['Gender']

    # Create or get Constituency object
    if constituency_name not in constituencies:
        constituency = Constituency(constituency_name, registered_voters, total_votes_cast, nation)
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

def display_menu():
    print("\nElection Data Inquiry System")
    print("1. Candidate Party")
    print("2. Candidate Name")
    print("3. Parliamentary Seat (Constituency Name)")
    print("4. Total Registered Voters in the Seat")
    print("5. Total Votes Cast in the Seat")
    print("6. Votes Cast for the Candidate")
    print("7. Votes for a Given Party as Percentage of Total Votes Cast")
    print("8. Average Votes Needed for a Candidate to be Elected")
    print("9. Average Percentage of Votes Needed for a Candidate to be Elected")
    print("10. Total Number of Female MPs")
    print("11. Percentage of Male and Female MPs Elected for Each Party")
    print("12. Exit and Save Statistics")
    choice = input("Enter your choice (1-12): ")
    return choice

def main_menu():
    while True:
        choice = display_menu()
        if choice == '1':
            # Candidate Party
            candidate_name = input("Enter candidate name: ")
            mp = next((mp for mp in mps if mp.name == candidate_name), None)
            if mp:
                print(f"{candidate_name} belongs to the {mp.party} party.")
            else:
                print(f"Candidate {candidate_name} not found.")
        elif choice == '2':
            # Candidate Name
            constituency_name = input("Enter constituency name: ")
            constituency = constituencies.get(constituency_name)
            if constituency and constituency.elected_mp:
                print(f"The elected MP for {constituency_name} is {constituency.elected_mp.name}.")
            else:
                print(f"No data for constituency {constituency_name}.")
        elif choice == '3':
            # Parliamentary Seat (Constituency Name)
            candidate_name = input("Enter candidate name: ")
            mp = next((mp for mp in mps if mp.name == candidate_name), None)
            if mp:
                print(f"{candidate_name} contested in the constituency {mp.constituency}.")
            else:
                print(f"Candidate {candidate_name} not found.")
        elif choice == '4':
            # Total Registered Voters in the Seat
            constituency_name = input("Enter constituency name: ")
            constituency = constituencies.get(constituency_name)
            if constituency:
                print(f"Total registered voters in {constituency_name}: {constituency.registered_voters}")
            else:
                print(f"No data for constituency {constituency_name}.")
        elif choice == '5':
            # Total Votes Cast in the Seat
            constituency_name = input("Enter constituency name: ")
            constituency = constituencies.get(constituency_name)
            if constituency:
                print(f"Total votes cast in {constituency_name}: {constituency.total_votes_cast}")
            else:
                print(f"No data for constituency {constituency_name}.")
        elif choice == '6':
            # Votes Cast for the Candidate
            candidate_name = input("Enter candidate name: ")
            mp = next((mp for mp in mps if mp.name == candidate_name), None)
            if mp:
                print(f"Votes received by {candidate_name}: {mp.votes_received}")
            else:
                print(f"Candidate {candidate_name} not found.")
        elif choice == '7':
            # Votes for a Given Party as Percentage of Total Votes Cast
            party_name = input("Enter party name: ")
            party = parties.get(party_name)
            if party:
                total_votes_cast = sum(c.total_votes_cast for c in constituencies.values())
                if total_votes_cast > 0:
                    percentage = (party.total_votes / total_votes_cast) * 100
                    print(f"{party_name} received {percentage:.2f}% of total votes cast.")
                else:
                    print("Total votes cast is zero.")
            else:
                print(f"Party {party_name} not found.")
        elif choice == '8':
            # Average Votes Needed for a Candidate to be Elected
            total_votes = sum(mp.votes_received for mp in mps if mp == constituencies[mp.constituency].elected_mp)
            total_mps = len([mp for mp in mps if mp == constituencies[mp.constituency].elected_mp])
            if total_mps > 0:
                average_votes = total_votes / total_mps
                print(f"Average votes needed for a candidate to be elected: {average_votes:.2f}")
            else:
                print("No data on elected MPs.")
        elif choice == '9':
            # Average Percentage of Votes Needed for a Candidate to be Elected
            percentages = []
            for constituency in constituencies.values():
                if constituency.elected_mp:
                    percent = (constituency.elected_mp.votes_received / constituency.total_votes_cast) * 100
                    percentages.append(percent)
            if percentages:
                average_percent = sum(percentages) / len(percentages)
                print(f"Average percentage of votes needed for a candidate to be elected: {average_percent:.2f}%")
            else:
                print("No data on elected MPs.")
        elif choice == '10':
            # Total Number of Female MPs
            female_mps = [mp for mp in mps if mp.gender.lower() == 'female' and mp == constituencies[mp.constituency].elected_mp]
            print(f"Total number of female MPs: {len(female_mps)}")
        elif choice == '11':
            # Percentage of Male and Female MPs Elected for Each Party
            for party_name, party in parties.items():
                gender_percentages = party.get_gender_percentage()
                print(f"Party: {party_name}")
                print(f"  Male MPs: {gender_percentages['male']:.2f}%")
                print(f"  Female MPs: {gender_percentages['female']:.2f}%")
        elif choice == '12':
            # Exit and Save Statistics
            save_statistics()
            print("Statistics saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def save_statistics():
    # Implement saving of statistics to a file
    # For example, write to a CSV file
    with open('election_statistics.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Constituency', 'Elected MP', 'Party', 'Votes Received', 'Percentage of Total Votes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for constituency in constituencies.values():
            if constituency.elected_mp:
                percentage = (constituency.elected_mp.votes_received / constituency.total_votes_cast) * 100
                writer.writerow({
                    'Constituency': constituency.name,
                    'Elected MP': constituency.elected_mp.name,
                    'Party': constituency.elected_mp.party,
                    'Votes Received': constituency.elected_mp.votes_received,
                    'Percentage of Total Votes': f"{percentage:.2f}%"
                })

if __name__ == "__main__":
    filename = input("Enter the election data filename (with extension): ")
    read_election_data(filename)
    main_menu()


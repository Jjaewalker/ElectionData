def display_menu():
    print("\nMenu Options:")
    print("1. View candidate details by party")
    print("2. View Candidate details by name")
    print("3. View Candidate details by Gender")
    print("4. View detail by constituency")
    print("5. View party performance")
    print("6. View Voting statistics")
    print("7. Plot party performance")
    print("8. Exit")

def handle_choice(choice, constituencies, parties):
    if choice == 1:
        party_name = input("enter party_name:")
        if party_name in parties:
            print(parties[party_name])
        else:
            print("party not found.")

    elif choice == 2:
        candidate_name = input("enter candidate name: ")
        found = False
        for constituency in constituencies.values():
            for candidate in constituencies.condidates:
                if  candidate.name.lower() == candidate_name.lower():
                    print(candidate)
                    found = True
                    break
            if found:
                break
        if not found:
            print("candidate not found.")

    elif choice == 3:
        constituency_name = input("Enter Constituency Name: ")
        if constituency_name in constituencies:  
            print(constituencies[constituency_name])
        else:
            print("Constituency not found.")

    elif choice == 4:
        for party in parties.values():
            print(party)

    elif choice == 5:
        total_votes = sum(c.votes_cast for c in constituencies.values())
        total_voters = sum(c.registered_voters for c in constituencies.values())
        print(f"Total votes cast: {total_votes}")
        print(f"Total registered voters: {total_voters}")
        print(f"Turnout: {total_votes / total_voters:.2%}")

    elif choice == 6:
        plot_party_performance(parties)

    elif choice == 7:
        save_statistics(parties)
        print("Statistics_saved. Exiting program.")
        exit()

    else:
        print("invalid choice. Please try again.")
def main():
    file_path = "xlsofdata.iml"
    constutuencies, parties = open(file_path)

    while True:
        display_menu()
        try: 
            choice = int(input("Enter your choice: "))
            handle_choice(choice, constutuencies, parties)
        except ValueError:
            print("invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
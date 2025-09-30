from linepunishment_writer import LinePunishmentWriter

def main():
    try:
        # Create a LinePunishmentWriter object
        punishment_sentence = "I will never spam my friends again."
        writer = LinePunishmentWriter(punishment_sentence, repetitions=10, typo_count=3)

        # Display all punishment sentences
        writer.display()

        # Print a summary using __str__
        print(writer)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

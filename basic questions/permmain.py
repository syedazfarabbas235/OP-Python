from permutation import PermutationGenerator

def main():
    try:
        # Input string "catdog"
        generator = PermutationGenerator("cat")
        generator.characters="abc"

        # Display all permutations
        generator.display()

        # Show summary using __str__
        print(generator)

    except TypeError as te:
        print(f"Type Error: {te}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

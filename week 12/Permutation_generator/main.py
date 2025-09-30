from permutation import PermutationGenerator

def main():
    try:
        # Input string "catdog"
        generator = PermutationGenerator("catdog")

        # Display all permutations
        generator.display()

        # Show summary using __str__
        print(generator)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

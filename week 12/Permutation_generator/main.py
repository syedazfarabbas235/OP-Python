from permutation import PermutationGenerator

def main():
    # Input string "catdog"
    generator = PermutationGenerator("catdog")

    # Display all permutations
    generator.display()

    # Show summary using __str__
    print(generator)

if __name__ == "__main__":
    main()

from bday_paradox import BirthdayParadox

def main():
    # Example runs
    bp1 = BirthdayParadox(group_size=23, simulations=100)
    bp1.show_probability()

    bp2 = BirthdayParadox(group_size=50, simulations=100)
    bp2.show_probability()

if __name__ == "__main__":
    main()

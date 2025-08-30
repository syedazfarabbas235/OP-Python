from bday_paradox import BirthdayParadox

def main():
    try:
        
         # Example runs
        bp1 = BirthdayParadox(group_size=23, simulations=30)
        bp1.show_probability()

        bp2 = BirthdayParadox(group_size=0, simulations=20) #raising error here
        bp2.show_probability()

    except (TypeError,ValueError) as e:
        print(f"error:{e}")

if __name__ == "__main__":
    main()

def main():
    """
    Main function to demonstrate the use of DivisionCounter class.
    """

    try:
        # Example 1: Initialize with a valid integer
        counter1 = DivisionCounter(64)
        counter1.display()                  # Display detailed report

        # Example 2: Using the copy constructor
        counter2 = DivisionCounter(counter1)
        counter2.display()
      

        # Example 3: Change the value using the setter
        counter2.value = 100
        counter2.display()
        
        # Example 4: Invalid input (less than 2)
        counter_invalid = DivisionCounter(2)  # This will raise ValueError


    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# ---------- Entry point ----------
if __name__ == "__main__":
    main()

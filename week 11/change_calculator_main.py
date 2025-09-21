from change_calculator import ChangeCalculator
def main():
    try:
        # Create calculator object
        calc = ChangeCalculator(103,120)
        calc.display()

        #copying calc
        calc2=ChangeCalculator(calc)
        calc2.display()
        
        calc3=ChangeCalculator(225,215)
        calc3.display()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

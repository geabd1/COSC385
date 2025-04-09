from binNumFunc import simulate_dfa

def main():
    while True:
        input_data = input("Enter a binary number: ")
        result = simulate_dfa(input_data)
        
        if result:
            print("Accepted")
            break  
        else:
            print("Not Accepted. Please enter a valid binary number (only 0s and 1s).")

if __name__ == "__main__":
    main()
import streamlit as st  
  
def calculate_percentage_difference(num1, num2):  
    try:  
        difference = abs(num1 - num2)  
        average = (num1 + num2) / 2  
        percentage_difference = (difference / average) * 100  
        return percentage_difference  
    except ZeroDivisionError:  
        return "Cannot calculate percentage difference with zero average."  
  
def main():  
    st.title("Percentage Difference Calculator")  
  
    st.write("Enter two numbers to calculate the percentage difference between them.")  
  
    # Input fields for the two numbers  
    num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")  
    num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")  
  
    # Calculate percentage difference  
    if st.button("Calculate"):  
        result = calculate_percentage_difference(num1, num2)  
        st.write(f"The percentage difference between {num1} and {num2} is: {result:.2f}%")  
  
if __name__ == "__main__":  
    main()  
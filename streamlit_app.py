import streamlit as st  
  
def calculate_percent_change(num1, num2):  
    try:  
        change = num2 - num1  
        percent_change = (change / num1) * 100  
        return percent_change  
    except ZeroDivisionError:  
        return "Cannot calculate percent change from zero."  
  
def main():  
    st.title("Percent Change Calculator")  
  
    st.write("Enter two numbers to calculate the percent change from the first to the second number.")  
  
    # Input fields for the two numbers (integers only)  
    num1 = st.number_input("Enter the first number", value=0, step=1)  
    num2 = st.number_input("Enter the second number", value=0, step=1)  
  
    # Calculate percent change and display the result automatically  
    result = calculate_percent_change(num1, num2)  
    if isinstance(result, str):  
        st.write(result)  
    else:  
        st.write(f"The percent change from {num1} to {num2} is: {result:.2f}%")  
  
if __name__ == "__main__":  
    main()  
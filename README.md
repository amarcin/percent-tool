# Percent Change Calculator

This is a simple web application built using Streamlit that calculates the percentage change from one number to another. It provides an intuitive interface for users to input numbers and instantly see the percentage change.

Open tool here: https://percent-tool.streamlit.app

## Features

- **User-Friendly Interface**: Easy to use with a clear input/output structure.
- **Instant Calculation**: Automatically calculates and displays the percent change as soon as the numbers are input.
- **Error Handling**: Accounts for division by zero and provides a helpful message.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system along with the Streamlit library. You can install Streamlit via pip:

```bash
pip install streamlit
```

### Running the App

To run the application, navigate to the directory containing the script and execute the following command:

```bash
streamlit run app.py
```

Replace `app.py` with the filename if it's different.

### Using the App

1. Enter the first number in the designated input field.
2. Enter the second number in the next field.
3. The application will automatically display the percentage change from the first number to the second.

## How It Works

- The app defines a function `calculate_percent_change` that computes the percentage change using the formula: 

  \[
  \text{Percent Change} = \left( \frac{\text{Change}}{\text{Initial Value}} \right) \times 100
  \]

- The app uses Streamlit to create a simple web interface with two input fields for numbers.
- The percent change is displayed immediately after the numbers are entered.

## Error Handling

- If the first number is zero, the app returns a message: "Cannot calculate percent change from zero."

## License

This project is open source and available for use under the MIT License.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Contact

For questions or feedback, you can reach out to the project maintainer.

---

Enjoy using the Percent Change Calculator!

import streamlit as st
import operator

# Initialize session state for calculation history
if 'history' not in st.session_state:
    st.session_state.history = []

def perform_calculation(num1, num2, operation):
    """
    Perform the specified arithmetic operation on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform
    
    Returns:
        tuple: (result, error_message)
    """
    operations = {
        'Addition (+)': operator.add,
        'Subtraction (-)': operator.sub,
        'Multiplication (×)': operator.mul,
        'Division (÷)': operator.truediv
    }
    
    try:
        if operation == 'Division (÷)' and num2 == 0:
            return None, "Error: Division by zero is not allowed"
        
        result = operations[operation](num1, num2)
        return result, None
    except Exception as e:
        return None, f"Error: {str(e)}"

def add_to_history(num1, num2, operation, result):
    """Add calculation to history."""
    operation_symbols = {
        'Addition (+)': '+',
        'Subtraction (-)': '-',
        'Multiplication (×)': '×',
        'Division (÷)': '÷'
    }
    
    calculation = f"{num1} {operation_symbols[operation]} {num2} = {result}"
    st.session_state.history.append(calculation)

def clear_history():
    """Clear calculation history."""
    st.session_state.history = []

# Main application
def main():
    st.title("🧮 Calculator")
    st.markdown("### Perform basic arithmetic operations")
    
    # Create two columns for input layout
    col1, col2 = st.columns(2)
    
    with col1:
        # First number input
        num1 = st.number_input(
            "First Number",
            value=0.0,
            format="%.6f",
            help="Enter the first number for calculation"
        )
    
    with col2:
        # Second number input
        num2 = st.number_input(
            "Second Number",
            value=0.0,
            format="%.6f",
            help="Enter the second number for calculation"
        )
    
    # Operation selection
    operation = st.selectbox(
        "Select Operation",
        ['Addition (+)', 'Subtraction (-)', 'Multiplication (×)', 'Division (÷)'],
        help="Choose the arithmetic operation to perform"
    )
    
    # Create columns for buttons
    button_col1, button_col2, button_col3 = st.columns([1, 1, 2])
    
    with button_col1:
        calculate_button = st.button("Calculate", type="primary")
    
    with button_col2:
        clear_button = st.button("Clear History")
    
    # Perform calculation when button is clicked
    if calculate_button:
        result, error = perform_calculation(num1, num2, operation)
        
        if error:
            st.error(error)
        else:
            st.success(f"**Result: {result}**")
            add_to_history(num1, num2, operation, result)
            st.rerun()
    
    # Clear history when button is clicked
    if clear_button:
        clear_history()
        st.success("History cleared!")
        st.rerun()
    
    # Display calculation history
    if st.session_state.history:
        st.markdown("---")
        st.markdown("### 📊 Calculation History")
        
        # Display history in reverse order (most recent first)
        for i, calculation in enumerate(reversed(st.session_state.history), 1):
            st.text(f"{len(st.session_state.history) - i + 1}. {calculation}")
    else:
        st.markdown("---")
        st.info("No calculations performed yet. Start by entering numbers and selecting an operation!")
    
    # Add some helpful information
    st.markdown("---")
    with st.expander("ℹ️ How to use this calculator"):
        st.markdown("""
        **Instructions:**
        1. Enter the first number in the "First Number" field
        2. Enter the second number in the "Second Number" field
        3. Select the desired operation from the dropdown menu
        4. Click the "Calculate" button to perform the operation
        5. View your result and calculation history below
        6. Use "Clear History" to reset the calculation history
        
        **Features:**
        - ✅ Basic arithmetic operations (addition, subtraction, multiplication, division)
        - ✅ Error handling for division by zero
        - ✅ Calculation history tracking
        - ✅ Input validation for numeric values
        - ✅ Clean and intuitive user interface
        
        **Supported Operations:**
        - **Addition (+)**: Adds two numbers
        - **Subtraction (-)**: Subtracts the second number from the first
        - **Multiplication (×)**: Multiplies two numbers
        - **Division (÷)**: Divides the first number by the second (with zero-division protection)
        """)

if __name__ == "__main__":
    main()

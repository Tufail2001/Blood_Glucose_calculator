import streamlit as st

# Function to calculate HbA1C based on average blood glucose
def calculate_hba1c(average_glucose):
    # Formula to estimate HbA1C from average blood glucose (mg/dL)
    hba1c = (average_glucose + 46.7) / 28.7
    return round(hba1c, 2)

# Function to provide health advice based on blood glucose levels
def health_advice(glucose_level):
    if glucose_level < 70:
        return "Your blood glucose level is low. Consider consuming some fast-acting carbs and consult your doctor."
    elif 70 <= glucose_level <= 140:
        return "Your blood glucose level is within the normal range. Keep maintaining a healthy lifestyle!"
    elif 141 <= glucose_level <= 199:
        return "Your blood glucose level is elevated (prediabetes range). Please consult your healthcare provider for further advice."
    else:
        return "Your blood glucose level is high. Please seek medical advice to manage your glucose levels effectively."

# Streamlit app interface
def main():
    st.title("Blood Glucose Assessment and HbA1C Estimator")

    # Input for blood glucose level
    glucose_level = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0, max_value=600, step=1)

    # Display health advice based on input
    if glucose_level > 0:
        advice = health_advice(glucose_level)
        st.subheader("Health Advice")
        st.write(advice)

        # Calculate and display estimated HbA1C
        hba1c = calculate_hba1c(glucose_level)
        st.subheader("Estimated HbA1C")
        st.write(f"Your estimated HbA1C is: {hba1c}%")

if __name__ == "__main__":
    main()

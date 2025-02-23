import streamlit as st

def main():
    st.title("Smart travel assistant")
    # create list of cities
    cities = ["Karachi", "Lahore", "Multan", "Islamabad"]
    # create dropdown list for cities
    destination = st.selectbox("Select your destined city", cities)
    # wether condition
    weather_condition = ["Sunny", "Rainy", "Cold"]
    # weather condition selection
    weather = st.selectbox("Select expected weather condition ", weather_condition)
    # display user selection
    st.write(f"you select city {destination} and expected weather {weather}")

    st.header("Expenses calculator")
    travel_days = st.number_input("Enter your travel days")
    daily_expenses = st.number_input("Enter your daily expenses")
    optional_expenses = st.number_input("add other expenses like flight, hotel etc. ")
    expenses = (travel_days * daily_expenses) + optional_expenses
    st.write(f"Estimated total cost to your destination {destination} for {travel_days} Days is {expenses}")

    # Task 3: Packing Checklist Generator
    st.header('Packing Checklist Generator')

    # Default packing lists based on weather condition
    packing_lists = {
        'Sunny': ['Sunglasses', 'Sunscreen', 'Hat'],
        'Rainy': ['Umbrella', 'Raincoat', 'Waterproof Shoes'],
        'Cold': ['Jacket', 'Gloves', 'Warm Clothes']
    }

    # Get the initial packing list based on selected weather
    # packing_list = packing_lists.get(weather, [])
    packing_list = packing_lists[weather]

    # Allow users to add or remove items
    modified_list = st.text_area('Modify your packing list:', value=", ".join(packing_list))
    final_packing_list = modified_list.split(", ")
    st.write('Your packing list:')
    for item in final_packing_list:
        st.write(f" {item}")

    if st.button("save travel plan"):
        with open("Travel plan.txt", "w") as file:
            file.write(f"selected city: {destination}\n" )
            file.write(f"expected weather: {weather}\n")
            file.write(f"Traveling Days: {travel_days}\n")
            file.write(f"expected cost: {expenses}\n")
            file.write(f"packing list: {final_packing_list}")

    

main()
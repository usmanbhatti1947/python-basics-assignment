# Define Dictionary

energy_consumption = {
    "Lights": 0.5,
    "AC": 1.5,
    "Fan": 0.3,
    "Heater": 2.0,
    "Refrigerator": 1.0,
    "Washer": 0.8
}
print("Initial power consumption usage", energy_consumption)

# Update Value

energy_consumption["Lights"] = 1.0
print("Updated Lights power consumption usage", energy_consumption)

# remove device energy usage

# energy_consumption["AC"] = 0      #By making it zero
# or get dynamic input 
device_to_remove = 'AC'           #Remove device
if device_to_remove in energy_consumption:
    del energy_consumption[device_to_remove]
else:
    print("input device not found in the list")

print("removed device AC ", energy_consumption)

#Total energy usage
total_energy_consumption = sum(energy_consumption.values())
print("Total energy consumption", total_energy_consumption)

power_saving_mode = {"Eco Mode", "Night Mode"}

# Add power saving mode 
power_saving_mode.add("Away Mode")
print("Away Mode added ", power_saving_mode)

# To check if mode is available
mode = "Night Mode"
if mode in power_saving_mode:
    print(f"{mode} is available in the set")
else:
    print("Mode is not available")

print("All power saving Modes ", power_saving_mode)








home1_devices = ['Lights', 'AC', 'Fan']
home2_devices = ['Fan', 'Door Lock', 'Lights']

def calculate_energy_cost(energy_usage, rate_per_kwh):
    monthly_cost = energy_usage * rate_per_kwh
    print("Total monthly energy cost: ",monthly_cost)


def common_devices(home1_devices, home2_devices):
    set_home1 = set(home1_devices)
    set_home2 = set(home2_devices)
    # converting in to set as set ignore duplicate values 
    common_devices = set_home1 & set_home2 # intersecting home1 & home2
    print("Common devices in both homes ", common_devices)

common_devices(home1_devices,home2_devices)

calculate_energy_cost(165, 0.12)
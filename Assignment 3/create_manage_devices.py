
devices_list = ["Fan", "AC", "Door Lock", "Thermostat"]

# Add a new device 
# insert value at first index by passing two arguments index and value
devices_list.insert(0,"Lights")

# add device at the last index by append
devices_list.append("Security camera")
print(devices_list)
# numbers = [1,2,3,4,5]
# numbers.extend([6,7,8,9]) #Add items at the end
# numbers.append([6,7,8,9])# add list at the end
# print(numbers)

# remove a device
# devices_list.remove("Thermostat")# by passing value
del devices_list[len(devices_list)-1]# can pass index as i pass last item by length
# devices_list.pop()# last item in list
devices_list.sort()# by default alphabetic order sort(reverse=False)
# devices_list.sort(reverse=True) # reverse alphabetic 

print(devices_list)

# tuple with device, status and power
devices_status=(
    ('AC', 'OFF', 1500), 
    ('Door Lock', 'ON', 0.5), 
    ('Fan', 'ON', 150), 
    ('Lights', 'ON', 60), 
    ('Thermostat', 'ON', 0.2),
)
for (device, status, watt) in devices_status:
    print(f"{device}:  status: {status} ,{watt} watt")
# def device_setting_status(devices_status):
#     for device in devices_status:
#         print(f" {device}")

# device_setting_status(devices_status)
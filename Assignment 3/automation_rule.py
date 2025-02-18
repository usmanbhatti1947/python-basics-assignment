def set_automation_rule(device, time, action):
    message = (f"Automation rule: {device} will be {action} at {time}")
    print(message)

set_automation_rule("Lights", "10:00 PM", "OFF")
# Output: "Automation Rule: Lights will be turned OFF at 10:00 PM."


devices = [("Lights", 60), ("AC", 1500), ("Fan", 40), ("Heater", 2000)]
def optimize_power(devices):
    active_devices = []
    for device, power in devices:
        if power <= 1000:
            active_devices.append(device)
    return active_devices

print(optimize_power(devices))
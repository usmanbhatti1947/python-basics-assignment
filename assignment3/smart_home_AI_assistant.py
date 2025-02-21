

def smart_home_assistant(name,*arg, **kwarg):
    print(f"{name}, checking status for", ", ".join(arg))
    
    for device, status in kwarg.items():
        print(f"{device} is {status}")


smart_home_assistant("Albert","Lights", "AC", Lights = "ON", AC = "OFF")
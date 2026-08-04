#Traffic light
#red=stop,yellow=warning,green=go
c=input("Ingresa un color: ").lower()
if c=="red":
    print("stop")
elif c==("green"):
    print("go")
elif c==("yellow"):
    print("warning")
else:
    print("invalid")

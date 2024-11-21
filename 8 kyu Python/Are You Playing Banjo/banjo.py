#codewars solution
'''
def are_you_playing_banjo(name):
    # Implement me! 
    if name.startswith("r") or name.startswith("R"):
        name = name + " plays banjo" 
    else:
        name = name + " does not play banjo"
    return name *
'''
#tested code 
name = input("podaj imie:")
if name.startswith("r") or name.startswith("R"):
        name = name + " plays banjo" 
else:
        name = name + " does not play banjo"
print(name)

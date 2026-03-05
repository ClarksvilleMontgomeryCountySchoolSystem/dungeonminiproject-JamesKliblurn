#You wake up on a cold stone floor. Your torch may be lit — and that changes everything.

#Create a boolean variable torch_lit
#Write a conditional statement with an else branch
#Inside each branch, define outcome as a string beginning with the correct prefix followed by your own creative text
#Use Flicker: for the success branch
#Use Doom: for the other branch
#Print outcome


torch_lit = True

if not torch_lit:
    outcome = "Doom: the darkness swallows you as dark creatures roam around nearbye"
else:
    outcome = "Flicker: the torch lights and a dark figure retreats into the shadows"

print(outcome)
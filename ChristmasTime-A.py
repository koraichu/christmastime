import datetime
from itertools import repeat
Eves = ()
Eve = ("Eve")

#The other comments in this chunk are for debug.
today = datetime.date.today()
#print("today:", today)
future = datetime.date((today.year),12,25)
#print("future:", future)
diff = future - today
#print("diff:", diff)

#For every day until Christmas, add another "EVE" to the string.
for i in range (diff.days):
 Eves = (Eve, Eves)
print ("It's Christmas ", str(Eves).replace("'", "",).replace("(", "").replace(")", "").replace(",", ""), "!!!")
print()
print(str(diff).replace(", 0:00:00", ""), "to go!")

#Wait for input to close program because Windows shell is stupid.
print()
print()
input("Press [RETURN] to exit.")

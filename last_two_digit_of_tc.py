from sys import argv
if "--help" in argv or "-h" in argv:
    print "Bu program ile TC numaranizin ilk 9 hanesini"
    print "yazdiginiz takdirde geri kalan 2 hanesini verir."
    quit()
firstnine = raw_input(":")
if len(firstnine) != 9 and firstnine.isdigit != True:
	quit()
singles = []
doubles = []
i = 0
if firstnine.isdigit() == True:
    while i != len(firstnine)-1:
        singles.append(int(firstnine[i]))
        i = i + 1
        doubles.append(int(firstnine[i]))
        i = i + 1
singles.append(int(firstnine[-1]))
tot = sum(singles)*7 -sum(doubles)
if tot >= 100:
    h = tot / 100
    tot = tot - (100 * h)
if tot >= 10:
    t = tot / 10
    tot = tot - (10 * t)
#print "10. Basamak --> " + str(tot)
   
tot11 = []

for i in range(len(firstnine)):
    tot11.append(int(firstnine[i]))
tot11.append(tot)
firstnine = firstnine + str(tot)
tot = sum(tot11)
 
if tot >= 100:
    h = tot / 100
    tot = tot - (100 * h)
if tot >= 10:
    t = tot / 10
    tot = tot - (10 * t)
#print "11.Basamak --> " + str(tot)
print "TC numaran:" + firstnine + str(tot)

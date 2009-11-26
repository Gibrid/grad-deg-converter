# -*- coding: cp1251 -*-

class angClk:
    def __init__(self, grds, mins, secs):
        self.grds = float(grds)
        self.mins = float(mins)
        self.secs = float(secs)

    def convert(self):
        return (self.secs/60 + self.mins)/60 + self.grds

class angDec:
    def __init__(self, dec):
        self.dec = float(dec)

    def getGrds(self):
        return math.floor(self.dec)

    def getMins(self):
        return math.floor(math.modf(self.dec)[0]*60)

    def getSecs(self):
        return math.modf(math.modf(self.dec)[0]*60)[0]*60

a1 = angClk(15, 12, 14)
a2 =angDec(10.2008333)

print "A1: %d\xb0 %d\' %3.2f\" is equal to: %f decimal" % (a1.grds, a1.mins, a1.secs, a1.convert())
print "A2: %f decimal is equal to %d\xb0 %d\' %3.2f\"" % (a2.dec, a2.getGrds(), a2.getMins(),a2.getSecs())


class Planet(object):
    def __init__(self, name, distance, orbitalPeriod=1.0):
        self.name = name
        self.distanceToSun = distanceToSun
        self.orbitalPeriod = orbitalPeriod

    def getDistanceToSun(self):
        return self.distanceToSun

    def getName(self):
        return self.name

    def getOrbitalPeriod(self):
        return self.orbitalPeriod

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun" .format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod())

    def setDistanceToSun(self, distance):
        self.distanceToSun = distance

    def setName(self, name):
        self.name = name

    def setOrbitalPeriod(self, orbitalPeriod):
        self.orbitalPeriod = orbitalPeriod

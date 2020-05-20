
class Planet(object):
    def __init__(self, name, distance, orbitalPeriod):
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


class Mercury(Planet):
    def __init__(self):
        Planet.__init__(self, "Mercury", 57900000, 0.24)
        self.diameter = 4879
        self.escapeVelocity = 4.3

    def getDiameter(self):
        return self.diameter

    def getEscapeVelocity(self):
        return self.escapeVelocity

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Mercury has a diameter of {} km and an escape velocity of {} km/s".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getDiameter(), self.getEscapeVelocity())

class Venus(Planet):
    def __init__(self):
        Planet.__init__(self, "Earth", 107500000, 0.615)
        self.gravity = 8.9
        self.density = 5243

    def getGravity(self):
        return self.gravity

    def getDensity(self):
        return self.density

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Venus has a gravity of {} m/s/s and a density of {} kg/m^3".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getGravity(), self.getDensity())

class Earth(Planet):
    def __init__(self):
        Planet.__init__(self, "Earth", 150000000, 1.0)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        return self.continentList

    def getOceans(self):
        return self.oceanList

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOceans(), self.getContinents())

class Mars(Planet):
    def __init__(self):
        Planet.__init__(self, "Mars", 227900000, 1.88)
        self.orbitalInclination = 1.9
        self.orbitalEccentricity = 0.094

    def getOrbitalInclination(self):
        return self.orbitalInclination

    def getOrbitalEccentricity(self):
        return self.orbitalEccentricity

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Mars has an orbital inclination of {} degrees and an orbital eccentricity of {}.".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOrbitalInclination(), self.getOrbitalEccentricity())

class Jupiter(Planet):
    def __init__(self):
        Planet.__init__(self, "Jupiter", 778600000, 11.86)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        return self.continentList

    def getOceans(self):
        return self.oceanList

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOceans(), self.getContinents())

class Saturn(Planet):
    def __init__(self):
        Planet.__init__(self, "Earth", 150000000, 1.0)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        return self.continentList

    def getOceans(self):
        return self.oceanList

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOceans(), self.getContinents())

class Uranus(Planet):
    def __init__(self):
        Planet.__init__(self, "Uranus", 150000000, 1.0)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        return self.continentList

    def getOceans(self):
        return self.oceanList

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOceans(), self.getContinents())

class Neptune(Planet):
    def __init__(self):
        Planet.__init__(self, "Neptune", 150000000, 1.0)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        return self.continentList

    def getOceans(self):
        return self.oceanList

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOceans(), self.getContinents())

class Pluto(Planet):
    def __init__(self):
        Planet.__init__(self, "Pluto", 150000000, 1.0)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        return self.continentList

    def getOceans(self):
        return self.oceanList

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. \n Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOceans(), self.getContinents())

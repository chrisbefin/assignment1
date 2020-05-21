class Planet(object):
    def __init__(self, name, distance, orbitalPeriod):
        self.name = name
        self.distanceToSun = distance
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
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Mercury has a diameter of {} km and an escape velocity of {} km/s".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getDiameter(), self.getEscapeVelocity())

class Venus(Planet):
    def __init__(self):
        Planet.__init__(self, "Venus", 107500000, 0.615)
        self.gravity = 8.9
        self.density = 5243

    def getGravity(self):
        return self.gravity

    def getDensity(self):
        return self.density

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Venus has a gravity of {} m/s/s and a density of {} kg/m^3".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getGravity(), self.getDensity())

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
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getOceans(), self.getContinents())

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
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Mars has an orbital inclination of {} degrees and an orbital eccentricity of {}.".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(), self.getOrbitalInclination(), self.getOrbitalEccentricity())

class Jupiter(Planet):
    def __init__(self):
        Planet.__init__(self, "Jupiter", 778600000, 11.86)
        self.dayLength = 9.9
        self.rotationPeriod = 9.9

    def getDayLength(self):
        return self.dayLength

    def getRotationPeriod(self):
        return self.rotationPeriod

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Jupiter has days that are {} hours long and a rotation period of {} hours".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getDayLength(), self.getRotationPeriod())

class Saturn(Planet):
    def __init__(self):
        Planet.__init__(self, "Saturn", 1433500000, 29.43)
        self.perihelion = 1352.6
        self.aphelion = 1514.5

    def getPerihelion(self):
        return self.perihelion

    def getAphelion(self):
        return self.aphelion

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Saturn has a perihelion of {} million km and a aphelion of {} million km.".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getPerihelion(), self.getAphelion())

class Uranus(Planet):
    def __init__(self):
        Planet.__init__(self, "Uranus", 2741300000, 83.76)
        self.meanTemp = -195
        self.numMoons = 27

    def getMeanTemp(self):
        return self.meanTemp

    def getNumMoons(self):
        return self.numMoons

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Uranus has an average temperature of {} degrees Celcius and {} moons.".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getMeanTemp(), self.getNumMoons())

class Neptune(Planet):
    def __init__(self):
        Planet.__init__(self, "Neptune", 4495100000, 163.75)
        self.diameter = 49528
        self.gravity = 11.0

    def getDiameter(self):
        return self.diameter

    def getGravity(self):
        return self.gravity

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Neptune has a diameter of {} km and gravity of {} m/s/s".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getDiameter(), self.getGravity())

class Pluto(Planet):
    def __init__(self):
        Planet.__init__(self, "Pluto", 5906400000, 247.98)
        self.surfacePressure = 0.00001
        self.isPlanet = False

    def getSurfacePressure(self):
        return self.surfacePressure

    def getIsPlanet(self):
        return self.isPlanet

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Pluto has a surface pressure of {} bars. Is Pluto an actual planet: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getSurfacePressure(), self.getIsPlanet())

class SolarSystem(object):
    def __init__(self):
        self.planets = [Mercury(), Venus(), Earth(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune(), Pluto()]

    def info(self):
        for planet in self.planets:
            print(planet.info())

    def getOrbits(self, days):
        for planet in self.planets:
            result = (days / 365.2) / planet.orbitalPeriod
            print("{} completes {} orbits in {} days." .format(planet.name, result, days))

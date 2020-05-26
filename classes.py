class Planet(object):
    """ Class which contains data for a planet
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self, name, distance, orbitalPeriod):
        self.name = name
        self.distanceToSun = distance #km
        self.orbitalPeriod = orbitalPeriod #earth years

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
    """ Class which contains data for Mercury, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            diameter: diameter of the planet in km<int>
            escapeVelocity: the planet's escape velocity in km/s<float>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getDiameter(): retrieves the diameter data member
                arguments: self
                returns: diameter<int>
            getEscapeVelocity(): retrieves the escapeVelocity data member
                arguments: self
                returns: escapeVelocity<float>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Mercury", 57900000, 0.24)
        self.diameter = 4879 #km
        self.escapeVelocity = 4.3 #km/s

    def getDiameter(self):
        return self.diameter

    def getEscapeVelocity(self):
        return self.escapeVelocity

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Mercury has a diameter of {} km and an escape velocity of {} km/s".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getDiameter(), self.getEscapeVelocity())

class Venus(Planet):
    """ Class which contains data for Venus, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            gravity: gravity of the planet in m/s/s<float>
            density: the planet's density in kg/m^3<int>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getGravity(): retrieves the gravity data member
                arguments: self
                returns: gravity<float>
            getDensity(): retrieves the density data member
                arguments: self
                returns: density<int>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Venus", 107500000, 0.615)
        self.gravity = 8.9 #m/s/s
        self.density = 5243 #kg/ m^3

    def getGravity(self):
        return self.gravity

    def getDensity(self):
        return self.density

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Venus has a gravity of {} m/s/s and a density of {} kg/m^3".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getGravity(), self.getDensity())

class Earth(Planet):
    """ Class which contains data for Earth, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            oceanList: list of Earth's oceans
            continentList: list of Earth's continents
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getContinents(): retrieves the continentList data member
                arguments: self
                returns: continentList<list of strings>
            getOceans(): retrieves the oceanList data member
                arguments: self
                returns: oceanList<list of strings>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Earth", 150000000, 1.0)
        self.oceanList = ["Pacific", "Atlantic", "Indian", "Southern", "Artic"]
        self.continentList = ["North America", "South America", "Antartica", "Africa", "Europe", "Asia", "Australia"]

    def getContinents(self):
        return self.continentList

    def getOceans(self):
        return self.oceanList

    def info(self):
        continents = ""
        oceans = ""
        for continent in self.continentList:
            continents = continents + continent + " "
        for ocean in self.oceanList:
            oceans = oceans + ocean + " "
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Earth has these oceans: {}, and these continents: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),oceans, continents)

class Mars(Planet):
    """ Class which contains data for Mars, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            orbitalInclination: orbital inclination of the planet in degrees<int>
            orbitalEccentricity: the planet's orbital eccentricity<float>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getOrbitalInclination(): retrieves the orbitalInclination data member
                arguments: self
                returns: orbtialInclination<int>
            getOrbitalEccentricity(): retrieves the orbitalEccentricity data member
                arguments: self
                returns: orbitalEccentricity<float>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Mars", 227900000, 1.88)
        self.orbitalInclination = 1.9 #degrees
        self.orbitalEccentricity = 0.094

    def getOrbitalInclination(self):
        return self.orbitalInclination

    def getOrbitalEccentricity(self):
        return self.orbitalEccentricity

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Mars has an orbital inclination of {} degrees and an orbital eccentricity of {}.".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(), self.getOrbitalInclination(), self.getOrbitalEccentricity())

class Jupiter(Planet):
    """ Class which contains data for Jupiter, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            dayLength: diameter of the planet in hours<float>
            rotationPeriod: the planet's rotation period in hours<float>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getDayLength(): retrieves the dayLength data member
                arguments: self
                returns: dayLength<float>
            getRotationPeriod(): retrieves the rotationPeriod data member
                arguments: self
                returns: rotationPeriod<float>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Jupiter", 778600000, 11.86)
        self.dayLength = 9.9 #hours
        self.rotationPeriod = 9.9 #hours

    def getDayLength(self):
        return self.dayLength

    def getRotationPeriod(self):
        return self.rotationPeriod

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Jupiter has days that are {} hours long and a rotation period of {} hours".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getDayLength(), self.getRotationPeriod())

class Saturn(Planet):
    """ Class which contains data for Saturn, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            perihelion: perihelion of the planet in km<int>
            aphelion: the planet's aphelion in km<int>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getPerihelion(): retrieves the perihelion data member
                arguments: self
                returns: perihelion<int>
            getAphelion(): retrieves the aphelion data member
                arguments: self
                returns: aphelion<int>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Saturn", 1433500000, 29.43)
        self.perihelion = 1352.6 #million km
        self.aphelion = 1514.5 #million km

    def getPerihelion(self):
        return self.perihelion

    def getAphelion(self):
        return self.aphelion

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Saturn has a perihelion of {} million km and a aphelion of {} million km.".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getPerihelion(), self.getAphelion())

class Uranus(Planet):
    """ Class which contains data for Uranus, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            meanTemp: mean temperature of the planet in degrees C<int>
            numMoons: the planet's number of moons<int>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getNumMoons(): retrieves the numMoons data member
                arguments: self
                returns: numMoons<int>
            getMeanTemp(): retrieves the meanTemp data member
                arguments: self
                returns: meanTemp<int>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Uranus", 2741300000, 83.76)
        self.meanTemp = -195 #deg C
        self.numMoons = 27

    def getMeanTemp(self):
        return self.meanTemp

    def getNumMoons(self):
        return self.numMoons

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Uranus has an average temperature of {} degrees Celcius and {} moons.".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getMeanTemp(), self.getNumMoons())

class Neptune(Planet):
    """ Class which contains data for Neptune, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            diameter: diameter of the planet in km<int>
            gravity: the planet's gravity in m/s/s<float>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getDiameter(): retrieves the diameter data member
                arguments: self
                returns: diameter<int>
            getGravity(): retrieves the gravity data member
                arguments: self
                returns: gravity<float>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Neptune", 4495100000, 163.75)
        self.diameter = 49528 #km
        self.gravity = 11.0 #m/s/s

    def getDiameter(self):
        return self.diameter

    def getGravity(self):
        return self.gravity

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Neptune has a diameter of {} km and gravity of {} m/s/s".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getDiameter(), self.getGravity())

class Pluto(Planet):
    """ Class which contains data for Pluto, inherits from the planet class
        data members:
            name: the name of the planet
            distanceToSun: the planet's distance from it's sun in km
            orbitalPeriod: time it takes for the planet to complete a revolution around its sun in earth years
            surfacePressure: surface pressure of the planet in bars<float>
            isPlanet: represents truth value of Pluto being a planet<bool>
        methods:
            __init__(): initializes object with passed values for data members
                arguments: self, name<string>, distance<int>, orbitalPeriod<float>
                returns: void
            getDistanceToSun(): retrieves the distanceToSun data member
                arguments: self
                returns: distanceToSun<int>
            getName(): retrieves the name data member
                arguments: self
                returns: name<string>
            getOrbitalPeriod(): retrieves the orbitalPeriod data member
                arguments: self
                returns: orbitalPeriod<float>
            getSurfacePressure(): retrieves the surfacePressure data member
                arguments: self
                returns: surfacePressure<float>
            getIsPlanet(): retrieves the isPlanet data member
                arguments: self
                returns: isPlanet<bool>
            info(): provides info regarding the planet
                arguments: self
                returns: sentence providing the planet's data<string>
            setDistanceToSun(): modifies the distanceToSun data member
                arguments: self, distance<int>
                returns: void
            setName(): modifies the name data member
                arguments: self, name<string>
                returns: void
            setOrbitalPeriod(): modifies the orbitalPeriod data member
                arguments: self, orbitalPeriod<float>
                returns: void
    """
    def __init__(self):
        Planet.__init__(self, "Pluto", 5906400000, 247.98)
        self.surfacePressure = 0.00001 #bars
        self.isPlanet = False #bool

    def getSurfacePressure(self):
        return self.surfacePressure

    def getIsPlanet(self):
        return self.isPlanet

    def info(self):
        return "The planet {} is {} km to its sun and takes {} Earth years to orbit its sun. Pluto has a surface pressure of {} bars. Is Pluto an actual planet: {}".format(self.getName(), self.getDistanceToSun(), self.getOrbitalPeriod(),self.getSurfacePressure(), self.getIsPlanet())

class SolarSystem(object):
    """ super class which contains an object for every planet in our solar system.
        data members:
            planets: list of objects for every planet in the solar system
        methods:
            __init__(): initializes planet list with objects
                arguments: self
                returns: void
            info(): prints out the information for every planet in the solar system
                arguments: self
                returns: void
            getOrbits(): prints out the number of orbits completed in a given number of Earth days for each planet in the solar system
                arguments: self, days<int>
                returns: void

    """
    def __init__(self):
        self.planets = [Mercury(), Venus(), Earth(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune(), Pluto()]

    def info(self):
        for planet in self.planets:
            print(planet.info())

    def getOrbits(self, days):
        for planet in self.planets:
            result = (days / 365.2) / planet.getOrbitalPeriod
            print("{} completes {} orbits in {} days." .format(planet.getName(), result, days))

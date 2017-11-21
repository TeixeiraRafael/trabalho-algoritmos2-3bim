class Street(object):
    def __init__(self, zipcode, name, nbhd):
        self.zipcode = zipcode
        self.name = name
        self.nbhd = nbhd

    def setZipCode(self, zipcode):
        self.zipcode = zipcode
    def setName(self, name):
        self.name = name
    def setNbhd(self, nbhd):
        self.nbhd = nbhd
    
    def getZipCode(self):
        return self.zipcode
    def getName(self):
        return self.name
    def getNbhd(self):
        return self.nbhd     
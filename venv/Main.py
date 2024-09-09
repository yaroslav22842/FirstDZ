class Human:
    def __init__(self, FirstName, LastName, Surname, PhoneNum, Country, City):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Surname = Surname
        self.PhoneNum = PhoneNum
        self.Country = Country
        self.City = City

    def setFirstName(self, newFirstName):
        self.FirstName = newFirstName

    def setLastName(self, newLastName):
        self.LastName = newLastName

    def setSurname(self, newSurname):
        self.Surname = newSurname

    def setPhoneNum(self, newPhoneNum):
        self.PhoneNum = newPhoneNum

    def setCountry(self, newCountry):
        self.Country = newCountry

    def setCity(self, newCity):
        self.City = newCity

    def showInfo(self):
        print(f"First name: {self.FirstName}")
        print(f"Last name: {self.LastName}")
        print(f"Surname: {self.Surname}")
        print(f"Phone number: {self.PhoneNum}")
        print(f"Country: {self.Country}")
        print(f"City: {self.City}")
        print("-----------------------------------------")

    def getFirstName(self):
        return self.FirstName

    def getGrade(self):
        return self.LastName

    def getMoney(self):
        return self.Surname

    def getIntelegence(self):
        return self.PhoneNum

    def getAge(self):
        return self.Country

    def getAge(self):
        return self.City

Person1 = Human("Taras", "Shevchenko", "Grigorievich", "+380 1234567890", "Ukraine", "Morintsy")
Person1.showInfo()

#             |
#             |
#             |
#             |
#             |
#             |
#             |
#             |
#             |
#             |
#             |
#             V






class City:
    def __init__(self, Title, Region, Country, Population, PostIndex, CityPhoneId):
        self.Title = Title
        self.Region = Region
        self.Country = Country
        self.Population = Population
        self.PostIndex = PostIndex
        self.CityPhoneId = CityPhoneId

    def setTitle(self, newTitle):
        self.Title = newTitle

    def setRegion(self, newRegion):
        self.Region = newRegion

    def setCountry(self, newCountry):
        self.Country = newCountry

    def setPopulation(self, newPopulation):
        self.Population = newPopulation

    def setPostIndex(self, newPostIndex):
        self.PostIndex = newPostIndex

    def setCityPhoneId(self, newCityPhoneId):
        self.CityPhoneId = newCityPhoneId

    def showInfo(self):
        print(f"Title: {self.Title}")
        print(f"Region: {self.Region}")
        print(f"Country: {self.Country}")
        print(f"Population: {self.Population}")
        print(f"Post index: {self.PostIndex}")
        print(f"City phone id: {self.CityPhoneId}")
        print("-----------------------------------------")

    def getTitle(self):
        return self.Title

    def getRegion(self):
        return self.Region

    def getCountry(self):
        return self.Country

    def getPopulation(self):
        return self.Population

    def getPostIndex(self):
        return self.PostIndex

    def getCityPhoneNumber(self):
        return self.CityPhoneId

City1 = City("Dnipro", "Europe", "Ukraine", "almost 1 Million", "49000", "+380")
City1.showInfo()



















































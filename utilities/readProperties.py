import configparser

# Create a ConfigParser object
config = configparser.RawConfigParser()
# Read the config.ini file
config.read("/Users/saurabh.sharma/PycharmProjects/pythonProjectPOM/Configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationUrl():
        url = config.get('URL', 'baseurl')
        print(url)
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('Credentials', 'username')
        return username

    @staticmethod
    def getUserPassword():
        password = config.get('Credentials', 'password')
        return password


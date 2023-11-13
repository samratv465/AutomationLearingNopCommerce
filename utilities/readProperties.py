import configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        userEmail = config.get('common info', 'username')
        return userEmail

    @staticmethod
    def getPassword():
        userPassword = config.get('common info', 'password')
        return userPassword
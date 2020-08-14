class SimpleModule():

    def __init__(self):
        self.text = 'hello'

    def printSomthing(self):
        result = self.get_value()
        return self.text + result

    def get_value(self):
        return 'gg'
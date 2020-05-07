class Model:

    def __init__(self, data):
        self.data = data

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]
        else:
            raise NameError("Undefined property.")

class SmartPhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
        print(f"Making a call")

    def play_music(self):
        print(f"Making a music")

    def install_app(self, name):
        print(f"{name} installed")


from kivy.app import App
from kivy.uix.label import Label
from plyer import gps

class GPSApp(App):
    def build(self):
        self.label = Label(text="Waiting for GPS data...")
        self.gps = gps
        self.gps.configure(on_location=self.update_location)
        self.gps.start(minTime=1000, minDistance=0)
        return self.label

    def update_location(self, **kwargs):
        latitude = kwargs.get('lat')
        longitude = kwargs.get('lon')
        accuracy = kwargs.get('accuracy')
        self.label.text = f"Latitude: {latitude}\nLongitude: {longitude}\nAccuracy: {accuracy} meters"

    def on_stop(self):
        self.gps.stop()

if __name__ == "__main__":
    GPSApp().run()

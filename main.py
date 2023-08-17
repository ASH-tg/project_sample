from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import gps
from plyer import permission

class LocationApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Waiting for location...")
        layout.add_widget(self.label)
        self.request_location_permission()
        return layout

    def request_location_permission(self):
        if permission.check_permission('location'):
            self.start_location_tracking()
        else:
            permission.request_permission('location', self.permission_callback)

    def permission_callback(self, permission, granted):
        if granted:
            self.start_location_tracking()
        else:
            self.label.text = "Location permission denied."

    def start_location_tracking(self):
        gps.configure(on_location=self.on_location)
        gps.start(minTime=1000, minDistance=1)

    def on_location(self, **kwargs):
        self.label.text = "Latitude: {}\nLongitude: {}".format(kwargs['lat'], kwargs['lon'])

if __name__ == '__main__':
    LocationApp().run()

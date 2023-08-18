from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.garden.mapview import MapView

from android.permissions import request_permission, Permission
from android import activity

class LocationApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Location: Waiting for permission...")
        self.button = Button(text="Get Location", on_press=self.get_location)
        self.map_view = MapView(lat=0, lon=0, zoom=1)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.map_view)
        return self.layout

    def get_location(self, instance):
        permission = Permission.ACCESS_FINE_LOCATION
        request_permission(permission, self.on_permission_result)

    def on_permission_result(self, permissions, grant_results):
        if all(result == Permission.GRANTED for result in grant_results):
            self.update_location()
        else:
            self.label.text = "Location permission denied."

    def update_location(self):
        gps = activity.getSystemService('gps')
        location = gps.getLastKnownLocation('gps')
        if location:
            latitude = location.getLatitude()
            longitude = location.getLongitude()
            self.label.text = f"Location: Latitude: {latitude}, Longitude: {longitude}"
            self.map_view.center_on(latitude, longitude)

if __name__ == "__main__":
    LocationApp().run()

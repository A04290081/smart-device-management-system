
class SmartDevice:
    def __init__(self, device_id, name):
        if not device_id:
            raise ValueError("Device ID cannot be empty.")
        self.__device_id = device_id
        self.__name = name
        self.__power_status = False  # False for off, True for on

    @property
    def device_id(self):
        return self.__device_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def power_status(self):
        return "On" if self.__power_status else "Off"

    def turn_on(self):
        if not self.__power_status:
            self.__power_status = True
            print(f"{self.__name} (ID: {self.__device_id}) turned ON.")
        else:
            print(f"{self.__name} (ID: {self.__device_id}) is already ON.")

    def turn_off(self):
        if self.__power_status:
            self.__power_status = False
            print(f"{self.__name} (ID: {self.__device_id}) turned OFF.")
        else:
            print(f"{self.__name} (ID: {self.__device_id}) is already OFF.")

    def display_info(self):
        return (f"Device ID: {self.__device_id}, Name: {self.__name}, "
                f"Power Status: {self.power_status}")


class TemperatureSensor(SmartDevice):
    def __init__(self, device_id, name, temperature=25.0):
        super().__init__(device_id, name)
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    def read_temperature(self):
        # Simulate reading temperature
        print(f"{self.name} (ID: {self.device_id}) current temperature: {self.__temperature}°C")
        return self.__temperature

    def display_info(self):
        return (f"{super().display_info()}, Type: Temperature Sensor, "
                f"Current Temperature: {self.__temperature}°C")


class SecurityCamera(SmartDevice):
    def __init__(self, device_id, name, recording_status=False):
        super().__init__(device_id, name)
        self.__recording_status = recording_status

    @property
    def recording_status(self):
        return "Recording" if self.__recording_status else "Not Recording"

    def start_recording(self):
        if not self.__recording_status:
            self.__recording_status = True
            print(f"{self.name} (ID: {self.device_id}) started recording.")
        else:
            print(f"{self.name} (ID: {self.device_id}) is already recording.")

    def stop_recording(self):
        if self.__recording_status:
            self.__recording_status = False
            print(f"{self.name} (ID: {self.device_id}) stopped recording.")
        else:
            print(f"{self.name} (ID: {self.device_id}) is not recording.")

    def display_info(self):
        return (f"{super().display_info()}, Type: Security Camera, "
                f"Recording Status: {self.recording_status}")


class SmartLight(SmartDevice):
    def __init__(self, device_id, name, brightness=50):
        super().__init__(device_id, name)
        self.__brightness = brightness

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, level):
        if 0 <= level <= 100:
            self.__brightness = level
            print(f"{self.name} (ID: {self.device_id}) brightness set to {self.__brightness}%")
        else:
            print("Brightness level must be between 0 and 100.")

    def increase_brightness(self, amount=10):
        new_brightness = min(100, self.__brightness + amount)
        self.brightness = new_brightness

    def decrease_brightness(self, amount=10):
        new_brightness = max(0, self.__brightness - amount)
        self.brightness = new_brightness

    def display_info(self):
        return (f"{super().display_info()}, Type: Smart Light, "
                f"Brightness: {self.__brightness}%")


# Function to display the menu
def display_menu():
    print("\n--- Smart Device Management System Menu ---")
    print("1. Display All Device Information")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature (for Temperature Sensors)")
    print("5. Adjust Brightness (for Smart Lights)")
    print("6. Start Recording (for Security Cameras)")
    print("7. Stop Recording (for Security Cameras)")
    print("8. Exit")
    print("------------------------------------------")


# Main program logic
def main():
    # Create instances of smart devices
    devices = [
        TemperatureSensor("TS001", "Living Room Sensor", 22.5),
        SmartLight("SL001", "Bedroom Light", 75),
        SecurityCamera("SC001", "Front Door Camera"),
        SmartLight("SL002", "Kitchen Light"),
    ]

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- All Device Information ---")
            for device in devices:
                print(device.display_info())
        elif choice == '2':
            device_id = input("Enter Device ID to turn ON: ")
            found = False
            for device in devices:
                if device.device_id == device_id:
                    device.turn_on()
                    found = True
                    break
            if not found:
                print("Device not found.")
        elif choice == '3':
            device_id = input("Enter Device ID to turn OFF: ")
            found = False
            for device in devices:
                if device.device_id == device_id:
                    device.turn_off()
                    found = True
                    break
            if not found:
                print("Device not found.")
        elif choice == '4':
            device_id = input("Enter Temperature Sensor ID to read temperature: ")
            found = False
            for device in devices:
                if device.device_id == device_id and isinstance(device, TemperatureSensor):
                    device.read_temperature()
                    found = True
                    break
            if not found:
                print("Temperature Sensor not found or invalid device ID.")
        elif choice == '5':
            device_id = input("Enter Smart Light ID to adjust brightness: ")
            found = False
            for device in devices:
                if device.device_id == device_id and isinstance(device, SmartLight):
                    try:
                        level = int(input(f"Enter new brightness level (0-100) for {device.name}: "))
                        device.brightness = level
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    found = True
                    break
            if not found:
                print("Smart Light not found or invalid device ID.")
        elif choice == '6':
            device_id = input("Enter Security Camera ID to start recording: ")
            found = False
            for device in devices:
                if device.device_id == device_id and isinstance(device, SecurityCamera):
                    device.start_recording()
                    found = True
                    break
            if not found:
                print("Security Camera not found or invalid device ID.")
        elif choice == '7':
            device_id = input("Enter Security Camera ID to stop recording: ")
            found = False
            for device in devices:
                if device.device_id == device_id and isinstance(device, SecurityCamera):
                    device.stop_recording()
                    found = True
                    break
            if not found:
                print("Security Camera not found or invalid device ID.")
        elif choice == '8':
            print("Exiting Smart Device Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

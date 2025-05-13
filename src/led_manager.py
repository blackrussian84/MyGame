class LEDManager:
    def __init__(self):
        self.led_state = False

    def turn_on(self):
        self.led_state = True
        self.update_led()

    def turn_off(self):
        self.led_state = False
        self.update_led()

    def update_led(self):
        if self.led_state:
            print("LED is ON")
        else:
            print("LED is OFF")

    def blink(self, times, interval):
        import time
        for _ in range(times):
            self.turn_on()
            time.sleep(interval)
            self.turn_off()
            time.sleep(interval)
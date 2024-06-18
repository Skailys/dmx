from dmx import DMX_Serial


class RelativeControl(DMX_Serial):
    """
    Represents a relative control for DMX_Serial.

    Attributes:
        x (int): The x v alue.
        xtrim (int): The x trim value.
        y (int): The y value.
        ytrim (int): The y trim value.
        xy_speed (int): The xy speed value.
    """

    def __init__(self, offset=0, port="/dev/ttyUSB0"):
        self.port = port
        self.offset = 0

        self.x = 0
        self.xtrim = 0
        self.y = 0
        self.ytrim = 0
        self.xy_speed = 0

        super().__init__()

    def add_x(self, value):
        self.x = overflow_add(self.x, value, 256)

    def add_y(self, value):
        self.y = overflow_add(self.y, value, 256)

    def add_xtrim(self, value):
        self.xtrim = overflow_add(self.xtrim, value, 256)

    def add_ytrim(self, value):
        self.ytrim = overflow_add(self.ytrim, value, 256)

    def add_xy_speed(self, value):
        self.xy_speed = overflow_add(self.xy_speed, value, 256)

    def set_x(self, value):
        assert 0 <= value <= 255
        self.x = value

    def set_y(self, value):
        assert 0 <= value <= 255
        self.y = value

    def set_xtrim(self, value):
        assert 0 <= value <= 255
        self.xtrim = value

    def set_ytrim(self, value):
        assert 0 <= value <= 255
        self.ytrim = value

    def set_xy_speed(self, value):
        assert 0 <= value <= 255
        self.xy_speed = value

    def get_data(self):
        offset = self.offset
        assert 0 <= offset <= 512 - 13  # 13 is the number of channels used by beam lamp

        data = [0] * 512
        data[0 + offset] = self.x
        data[1 + offset] = self.xtrim
        data[2 + offset] = self.y
        data[3 + offset] = self.ytrim
        data[4 + offset] = self.xy_speed

        return bytes(data)

    def send(self):
        self.set_data(self.get_data())

    def start(self):
        super().start()

    def stop(self):
        super().stop()

def overflow_add(a, b, max_value):
    return (a + b) % max_value
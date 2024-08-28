import random
import sys

class TestHelper:
    @staticmethod
    def gimme_sample_notes(count: int, xRange: int, yRange: int):
        data = []
        for _ in range(count):
            x_value = random.randint(0, xRange)
            y_value = random.randint(0, yRange)
            data.append((x_value, y_value))
        return data
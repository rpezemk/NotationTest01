import random
import sys

class TestHelper:
    @staticmethod
    def gimme_sample_notes(count: int):
        data = []
        for _ in range(count):
            x_value = random.randint(0, 50)
            y_value = random.randint(0, 100)
            data.append((x_value, y_value))
        return data
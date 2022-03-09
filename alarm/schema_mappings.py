from enum import Enum


class Captcha(Enum):
    DEFAULT = -1
    DISABLED = 0



    def __init__(self, bit: int) -> None:
        super().__init__()

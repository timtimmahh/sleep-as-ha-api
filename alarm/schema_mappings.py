from enum import Enum, auto, unique, IntEnum, IntFlag
from datetime import datetime

import voluptuous as vol


def Datetime():
    return lambda time_in_ms: datetime.utcfromtimestamp(time_in_ms)


class DaysOfWeek(IntFlag):
    MONDAY = 0x01
    TUESDAY = 0x02
    WEDNESDAY = 0x04
    THURSDAY = 0x08
    FRIDAY = 0x10
    SATURDAY = 0x20
    SUNDAY = 0x40


class Repeat(IntEnum):
    NONE = -1
    WEEKLY = 0
    ODD_WEEK = 1
    EVEN_WEEK = 2
    NON_WEEKLY = 3

    def __new__(cls, days: int, non_weekly_from: int, non_weekly_repeat: int, week_repeat: int):
        obj = int.__new__(cls, week_repeat)
        if week_repeat == 3:
            obj.times = non_weekly_repeat
            obj.start_from = \
                datetime.utcfromtimestamp(non_weekly_from).astimezone() \
                if non_weekly_from > -1 \
                else None
        else:
            obj.times = DaysOfWeek(days)
            obj.start_from = -1
        return obj


@unique
class Captcha(Enum):
    DEFAULT = -1
    DISABLED = 0

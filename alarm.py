import voluptuous as vol

from alarm.schema_mappings import Datetime

SCHEMA = vol.Schema({
    vol.Required("id", default=-1): vol.Number(),
    vol.Required("hour"): vol.Number(),
    vol.Required("minutes"): vol.Number(),
    vol.Required("daysOfWeek"): {
        vol.Required("days"): vol.Number(),
        vol.Optional("nonWeeklyFrom", default=-1): Datetime(),
        vol.Optional("nonWeeklyRepeat", default=-1): vol.Number(),
        vol.Optional("weekRepeat", default=0): vol.Number()
    },
    vol.Optional("label"): str,
    vol.Optional("enabled", default=True): vol.Boolean(),
    vol.Optional("silent", default=False): vol.Boolean(),
    vol.Optional("vibrate", default=True): vol.Boolean(),
    vol.Optional("captcha", default=-1): vol.Number(),
    vol.Optional("alert"): str,
    vol.Optional("extendedConfig"): {
        vol.Optional("terminatesTracking", default=True): vol.Boolean(),
        vol.Optional("gradualVolumeIncrease", default=-2): vol.Number(),
        vol.Optional("isSelfDisposable", default=False): vol.Boolean(),
        vol.Optional("lastEnableTimestamp"): Datetime(),
        vol.Optional("selectedPlaylists", default=[]): [str],
        vol.Optional("snoozeAfterAlarm", default=-1): vol.Number(),
        vol.Optional("snoozeDuration", default=5): vol.Number(),
        vol.Optional("snoozeLimit", default=-2): vol.Number(),
        vol.Optional("snoozeTotalTimeLimit", default=-2): vol.Number(),
        vol.Optional("soundDelay", default=-2): vol.Number(),
        vol.Optional("terminatesTracking", default=True): vol.Boolean(),
        vol.Optional("timeToBed", default=-2): vol.Number(),
        vol.Optional("vibrationStart", default=0): vol.Number(),
        vol.Optional("vibrationStartSmartWatch", default=0): vol.Number(),
        vol.Optional("weekRepeat", default=0): vol.Number(),
    },
    vol.Optional("suspendTime", default=-1): Datetime(),
    vol.Optional("time"): Datetime()
}, extra=True)


class SleepAlarm:

    def __init__(self, data) -> None:
        super().__init__()
        self.data = SCHEMA(data)


class AlarmDaysOfWeek:
    WEEK_REPEAT = [
        'Weekly',
        'Odd Week',
        'Even Week',
        'Non-Weekly'
    ]

    def __init__(self, data) -> None:
        super().__init__()
        self.days: int = data['days']
        self.non_weekly_from: int = data['nonWeeklyFrom']
        self.non_weekly_repeat: int = data['nonWeeklyRepeat']
        self.week_repeat: int = data['weekRepeat']

    def convert_days(self):
        return [
            0x01 & self.days == 1,  # Monday
            0x02 & self.days == 1,  # Tuesday
            0x04 & self.days == 1,  # Wednesday
            0x08 & self.days == 1,  # Thursday
            0x10 & self.days == 1,  # Friday
            0x20 & self.days == 1,  # Saturday
            0x40 & self.days == 1  # Sunday
        ]

    def convert_week_repeat(self):
        return self.WEEK_REPEAT[self.week_repeat]

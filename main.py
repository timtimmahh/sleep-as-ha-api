from datetime import datetime

to_date = lambda ts: datetime.fromtimestamp(ts)
to_str = lambda label: label if isinstance(label, str) else str(label)

EVENTS = {
    "sleep_tracking_started": tuple(),  # Fires when sleep tracking starts.
    "sleep_tracking_stopped": tuple(),  # Fires when sleep tracking stops.
    "sleep_tracking_paused": tuple(),  # Fires when sleep tracking paused.
    "sleep_tracking_resumed": tuple(),  # Fires when sleep tracking resumed.
    "alarm_snooze_clicked": (to_date, to_str),  # You have snoozed a ringing alarm.
    "alarm_snooze_canceled": (to_date, to_str),  # You have a canceled an alarm that is currently snoozed.
    "time_to_bed_alarm_alert": (to_date,),  # Fires when you get a bedtime notification.
    "alarm_alert_start": (to_date, to_str),  # Fires when alarm starts.
    "alarm_alert_dismiss": (to_date, to_str),  # Fires when you dismiss alarm (after you solve CAPTCHA if it’s set).
    "alarm_skip_next": (to_date, to_str),  # Fires when you tap dismiss an alarm from notification before it
    # actually rings.
    "show_skip_next_alarm": (to_date,),  # Fires exactly 1 hour before the next alarm is triggered.
    "rem": tuple(),  # Fires when we estimate the start of REM phase.
    "smart_period": tuple(),  # Fires at the start of the smart period.
    "before_smart_period": (to_str,),  # Fires 45 minutes before the start of smart period.
    "lullaby_start": tuple(),  # Fires when lullaby starts playing.
    "lullaby_stop": tuple(),  # Fires when lullaby is stopped (either manually or automatically).
    "lullaby_volume_down": tuple(),  # Fires when we detect you fell asleep and starting lowering the
    # volume of lullabies.
    "deep_sleep": tuple(),  # Fires when we detect you going into deep sleep phase.
    "light_sleep": tuple(),  # Fires when we detect you going into light sleep phase.
    "awake": tuple(),  # Fires when we detect you woke up.
    "not_awake": tuple(),  # Fires when we detect you fell asleep.
    "apnea_alarm": tuple(),  # Fires when we detect a significant dip in your oxygen levels.
    "antisnoring": tuple(),  # Fires when antisnoring is triggered.
    "sound_event_snore": tuple(),  # Fires when we detect snoring.
    "sound_event_talk": tuple(),  # Fires when we detect talking.
    "sound_event_cough": tuple(),  # Fires when we detect coughing.
    "sound_event_baby": tuple(),  # Fires when we detect baby cry.
    "sound_event_laugh": tuple()  # Fires when we detect laughter.
}


class SleepEvent:

    def __init__(self, event: str, *values) -> None:
        super().__init__()
        self.event = event
        self.values = values


def handle_webhook(data):
    event = data['event']
    values = [conv(data[f'value{i}']) for i, conv in enumerate(EVENTS[event])]
    return SleepEvent(event, *values)


if __name__ == '__main__':
    pass

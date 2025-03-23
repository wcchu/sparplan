from Sparplan import logger
from datetime import datetime, timedelta


class Gardener:
    def __init__(self, config):
        self.start_date = datetime.fromisoformat(config["start_date"].get(str)).date()
        self.end_date = datetime.fromisoformat(config["end_date"].get(str)).date()
        self.plant_schedule = config["plant_schedule"].get(str)

    def work(self, _):
        interval = (self.end_date - self.start_date).days
        logger.info("interval = {} days".format(interval))

        for days_ in range(interval + 1):
            now_date = self.start_date + timedelta(days_)
            if self.plant_today(now_date, self.plant_schedule):
                logger.info("scheduled planting today {}".format(now_date))

    @staticmethod
    def plant_today(today, schedule):
        """
        Return whether today is on the planting schedule.

        Args:
            today: datetime.date()
            schedule: str

        Returns: bool
        """
        if (schedule == "weekly") & (today.isoweekday() == 1):
            return True
        elif (schedule == "monthly") & (today.day == 1):
            return True
        return False

    def plant(self, amount):
        pass

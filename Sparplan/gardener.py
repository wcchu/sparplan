from Sparplan import logger
from datetime import date, timedelta


class Gardener:
    def __init__(self, config):
        self.start_date = date.fromisoformat(config["start_date"].get(str))
        self.end_date = date.fromisoformat(config["end_date"].get(str))
        self.seeds = config["start_seeds"].get(float)
        self.plant_schedule = config["plant_schedule"].get(str)
        self.plant_amount = config["plant_amount"].get(float)
        self.flowers = 0.0

    def work(self, data):
        interval = ((self.end_date - self.start_date)).days
        logger.info("interval = {} days".format(interval))

        for days_ in range(interval + 1):
            now_date = self.start_date + timedelta(days_)
            if self.plant_today(now_date, self.plant_schedule):
                logger.info(
                    "plant on {} with seeds = {} and flowers = {}".format(
                        now_date, self.seeds, self.flowers
                    )
                )
                self.plant(data, now_date)

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

    def plant(self, data, scheduled_date):
        value = -1.0
        shift = 0
        while value < 0.0:
            checked_date = scheduled_date + timedelta(shift)
            value = data.get(str(checked_date), -1.0)
            shift = shift + 1
        logger.info("got value on {}, at {}".format(checked_date, value))

        self.seeds = self.seeds - self.plant_amount
        flower_amount = self.plant_amount / value
        self.flowers = self.flowers + flower_amount
        logger.info(
            "convert {} seeds to {} flowers".format(self.plant_amount, flower_amount)
        )

        return

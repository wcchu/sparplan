from Sparplan import logger
from datetime import date, timedelta


class Gardener:
    def __init__(self, config):
        self.start_date = date.fromisoformat(config["start_date"].get(str))
        self.end_date = date.fromisoformat(config["end_date"].get(str))
        self.plant_schedule = config["plant_schedule"].get(str)
        self.seeds_used = 0.0
        self.flowers_grown = 0.0

    def work(self, data):
        if str(self.start_date) < min(list(data.keys())):
            raise ValueError(
                "start date {} earlier than available data".format(self.start_date)
            )
        if str(self.end_date) > max(list(data.keys())):
            raise ValueError(
                "end date {} later than available data".format(self.end_date)
            )

        interval = ((self.end_date - self.start_date)).days
        logger.debug("interval = {} days".format(interval))

        for days_ in range(interval + 1):
            now_date = self.start_date + timedelta(days_)
            if self.day_on_schedule(now_date, self.plant_schedule):
                logger.debug(
                    "date = {}, total seeds used = {}, total flowers grown = {}".format(
                        now_date, self.seeds_used, self.flowers_grown
                    )
                )
                value = self.find_value(data, now_date)
                self.plant(value)

    def final_report(self, data):
        initial_value = self.find_value(data, self.start_date)
        final_value = self.find_value(data, self.end_date)
        total_flowers_value = self.flowers_grown * final_value
        rel_gain = (total_flowers_value / self.seeds_used) - 1.0
        rel_value_change = (final_value / initial_value) - 1.0
        logger.info("relative value change = {:.6f}".format(rel_value_change))
        logger.info("relative gain = {:.6f}".format(rel_gain))
        return

    @staticmethod
    def day_on_schedule(today, schedule):
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

    @staticmethod
    def find_value(data, aim_date):
        logger.debug("trying to find value on {}".format(aim_date))
        value = -1.0
        shift = 0
        while value < 0.0:
            checked_date = aim_date + timedelta(shift)
            value = data.get(str(checked_date), -1.0)
            shift = shift + 1
        logger.debug("got value {} on {}".format(value, checked_date))
        return value

    def plant(self, value):
        self.seeds_used = self.seeds_used + 1.0
        new_flowers = 1.0 / value
        self.flowers_grown = self.flowers_grown + new_flowers
        logger.debug("convert a seed to {} flowers".format(new_flowers))
        return

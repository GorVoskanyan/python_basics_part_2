import datetime

class Date:
    def __init__(self, day, month, year):
        self.d = day
        self.m = month
        self.y = year

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return date_obj

    @classmethod
    def is_valid_date(cls, date):
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999

    def __str__(self) -> str:
        return f"{self.d:02d}/{self.m:02d}/{self.y:04d}"



if __name__ == '__main__':
    date_obj1 = Date.from_string('06-11-2024')
    print(date_obj1) # -> 06/11/2024
    print(Date.is_valid_date('06-11-2024'))  # -> True
    print(Date.is_valid_date('36-11-2024'))  # -> False
    current_time = datetime.datetime.now(datetime.UTC)
    print(current_time)
    # https: // docs.python.org / 3.12 / library / datetime.html  # datetime.datetime.now
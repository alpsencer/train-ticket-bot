from WebQuery import WebQuery


class TicketQuery:
    # STATIONS = WebQuery
    def __init__(self, fro, to, start_date, end_date, ID):
        self.fro = fro
        self.to = to
        self.start_date = start_date
        self.end_date = end_date
        self.ID = ID


class Ticket:
    def __init__(self, train_list, cost, travel_time):
        self.train_list = train_list
        self.fro = train_list[0].fro
        self.to = train_list[-1].to
        self.start_date = train_list[0].start_date
        self.start_hour = train_list[0].start_hour
        self.end_date = train_list[-1].end_date
        self.end_hour = train_list[-1].end_hour
        self.cost = cost
        self.travel_time = travel_time


class Train:
    def __init__(self, fro, to, start_date, start_hour, end_date, end_hour, available_seat):
        self.fro = fro
        self.to = to
        self.start_date = start_date
        self.start_hour = start_hour
        self.end_date = end_date
        self.end_hour = end_hour
        self.available_seat = available_seat

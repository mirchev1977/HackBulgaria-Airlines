class Flight():
    """docstring for ClassName"""

    def __init__(
            self, start_time, end_time, passengers,
            max_passengers, from_dest,
            to_dest, terminal, declined):

        self.start_time = start_time
        self.end_time = end_time
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined

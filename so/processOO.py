class Process:
    def __init__(self, number, arrival, peak, wTime = 0, \
        taTime = 0, rTime = 0):
        self.number = number
        self.arrival = arrival
        self.peak = peak
        self.wTime = wTime
        self.taTime = taTime
        self.rTime = rTime
    

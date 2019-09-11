class Process:
    def __init__(self, number, arrival, peak, wTime = 0, \
        taTime = 0, rTime = 0):
        self.number = number
        self.arrival = arrival
        self.peak = peak
        self.wTime = wTime
        self.taTime = taTime
        self.rTime = rTime
        self.rPeak = peak

    def printa(self):
        print("Number:", self.number)
        print("Arrival:", self.arrival)
        print("Peak:", self.peak)
        print("wTime:", self.wTime)
        print("taTime:", self.taTime)
        print("rTime:", self.rTime)
        print("rPeak:", self.rPeak)
        print("- - - - - - - - -")
    

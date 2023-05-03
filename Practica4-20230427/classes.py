class Activity:
    def __init__(self, name, duration, participation, total_price, cost):
        self.name =name
        self.duration = duration
        self.participation = participation
        self.total_price = total_price
        self.cost = cost

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_duration(self):
        return self.duration
    
    def set_duration(self, duration):
        self.duration = duration
    
    def get_participation(self):
        return self.participation
    
    def set_participation(self, participation):
        self.participation = participation
    
    def get_total_price(self):
        return self.total_price
    
    def set_total_price(self, total_price):
        self.total_price = total_price
    
    def get_cost(self):
        return self.cost
    
    def set_cost(self, cost):
        self.cost = cost
        
    def __str__(self):
        return f"({self.duration} min, {self.participation} participantes, ${self.total_price})"


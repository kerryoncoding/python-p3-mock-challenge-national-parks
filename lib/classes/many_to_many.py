class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, 'name'):
            if isinstance(value, str) and (2 < len(value)):
                self._name = value 
        
    def trips(self):
        pass

    def visitors(self):
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass


class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.vistor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and (6 < len(value)):
            # need to figure out this: start_date is in the format "September 1st" 
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and (6 < len(value)):
            # need to figure out this: end_date is in the format "September 1st" 
            self._end_date = value

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        if isinstance(value, Visitor):
            self._visitor = value
    


    

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and (0 < len(value) < 16):
            self._name = value 
        
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass
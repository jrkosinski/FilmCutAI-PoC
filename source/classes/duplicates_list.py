
class DuplicatesList: 
    def __init__(self): 
        self.duplicates = {}

    def add(self, key, value): 
        if (key not in self.duplicates.keys()): 
            self.duplicates[key] = { }
        self.duplicates[key][value] = True
            
        #add the inverse as well 
        if (value not in self.duplicates.keys()): 
            self.duplicates[value] = { }
        self.duplicates[value][key] = True
        
    def are_duplicates(self, key1, key2): 
        return key1 in self.duplicates.keys() and key2 in self.duplicates.keys() and key1 in self.duplicates[key2].keys()

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

# GETTING THE INDEX OF THE KEY    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_list(self):
        for i, v in enumerate(self.data_map):
            print(i, ":", v)

# SETTING THE VALUES IN THE HASH MAP    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] 
        self.data_map[index].append([key, value])   

# FOR GETTING THE VALUE OF THE KEY AT THE PARTICULAR INDEX
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None             

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
          


My_hash_table = HashTable()
My_hash_table.set_item("anand", 21)
My_hash_table.set_item("aman",20)
My_hash_table.set_item("anjali",1)
# print(My_hash_table.get_item("anand"))
print(My_hash_table.keys())

My_hash_table.print_list()            
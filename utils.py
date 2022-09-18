class MapUtils():

    @staticmethod
    def check_in_map_list_yellow(m, k, v):
        if k in m and v in m[k]:
            return False
        elif k in m.keys():
            return True
        return -1

    @staticmethod
    def add_to_mapvalue_list(m, k, v):
        if k in m.keys():
            m[k].append(v)
        else:
            m[k] = [v]   

    @staticmethod
    def increment_map_value(m, k):
        if k in m.keys():
            m[k] += 1
        else:
            m[k] = 1

    @staticmethod
    def get_from_map_nullsafe(m, k):
        if k not in m.keys():
            return -1
        else:
            return m[k]
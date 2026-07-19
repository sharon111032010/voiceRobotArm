import re


class CommandParser:


    def __init__(self):

        self.num_map = {
            "一":1,
            "二":2,
            "三":3,
            "四":4,
            "五":5,
            "六":6
        }


    def parse(self,text):

        pattern = r"第([一二三四五六])格.*?第([一二三四五六])格"


        result = re.search(pattern,text)


        if result is None:
            return None


        start = self.num_map[result.group(1)]
        end = self.num_map[result.group(2)]


        return start,end
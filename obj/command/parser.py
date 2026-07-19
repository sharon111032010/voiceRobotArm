import re


class CommandParser:


    def __init__(self):

        self.num_map = {

            "一":1,
            "二":2,
            "三":3,
            "四":4,
            "五":5,
            "六":6,

            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6
        }



    def convert_number(self, value):

        return self.num_map.get(value)



    def parse(self,text):

        print("解析文字:", text)


        # 支援:
        # 第三項
        # 第3項
        # 第三格
        # 第3格
        # 第三個

        pattern = (
            r"第([一二三四五六123456])"
            r"[格項個線]?"
            r".*?"
            r"第([一二三四五六123456])"
            r"[格項個線]?"
        )


        result = re.search(
            pattern,
            text
        )


        if result is None:

            return None



        start = self.convert_number(
            result.group(1)
        )


        end = self.convert_number(
            result.group(2)
        )


        return start,end
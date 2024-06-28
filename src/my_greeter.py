import datetime

class MyGreeter:
    def greeting(self):
        current_time = datetime.datetime.now().time()
        
        time_ranges = {
            (datetime.time(6, 0), datetime.time(12, 0)): "Good morning",
            (datetime.time(12, 0), datetime.time(18, 0)): "Good afternoon"
        }
        
        # 找到当前时间所属的时间段，并返回对应的问候语
        for range_times, greeting_msg in time_ranges.items():
            start_time, end_time = range_times
            if start_time <= current_time < end_time:
                return greeting_msg
        
        # 返回 "Good evening"
        return "Good evening"



if __name__ == "__main__":
    m = MyGreeter()
    print(m.greeting())
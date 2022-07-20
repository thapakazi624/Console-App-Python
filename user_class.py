# defining a class for the course that user enrols

class Courseclass():
    def __init__(self, course_enrolled):
        self.course_enrolled = course_enrolled
        self.all_user_info = []


    def display_userinfo(self):
        for user in self.all_user_info:
            print(user)
    def data_log(self):
        data = self.all_user_info
        return data


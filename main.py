import datetime

class JobApplication:
    def __init__(self, first_name, last_name, dob, address, prev_job_exp):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.address = address
        self.prev_job_exp = prev_job_exp

    def validate_dob(self):
        try:
            datetime.datetime.strptime(self.dob, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_address(self):
        if len(self.address.split(',')) != 2:
            return False
        return True

    def validate_prev_job_exp(self):
        if len(self.prev_job_exp) < 3:
            return False
        return True

    def submit_application(self):
        if self.validate_dob() and self.validate_address() and self.validate_prev_job_exp():
            print("Application submitted successfully.")
        else:
            print("Application submission failed. Please check your information and try again.")

app = JobApplication("John", "Doe", "1995-01-01", "123 Main St, Anytown USA", ["Software Developer at XYZ Company (2018-2020)", "Python Developer at ABC Company (2020-2022)"])
app.submit_application()

from fpdf import FPDF

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

    def save_to_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Job Application", ln=1, align="C")
        pdf.cell(200, 10, txt="Name: {} {}".format(self.first_name, self.last_name), ln=1)
        pdf.cell(200, 10, txt="Date of Birth: {}".format(self.dob), ln=1)
        pdf.cell(200, 10, txt="Address: {}".format(self.address), ln=1)
        pdf.cell(200, 10, txt="Previous Job Experience:", ln=1)
        for exp in self.prev_job_exp:
            pdf.cell(200, 10, txt="- {}".format(exp), ln=1)
        pdf.output("job_application.pdf")

    def submit_application(self):
        if self.validate_dob() and self.validate_address() and self.validate_prev_job_exp():
            self.save_to_pdf()
            print("Application submitted successfully.")
        else:
            print("Application submission failed. Please check your information and try again.")

app = JobApplication("John", "Doe", "1995-01-01", "123 Main St, Anytown USA", ["Software Developer at XYZ Company (2018-2020)", "Python Developer at ABC Company (2020-2022)"])
app.submit_application()

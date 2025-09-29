import os

class SignupPage:
    def __init__(self, page, base_url=None):
        self.page = page
        self.base_url = base_url or os.getenv("APP_URL", "http://localhost:5173")
        self.signup_input_username = page.get_by_placeholder('Username')
        self.signup_input_password = page.get_by_placeholder('Password')
        self.signup_btn_signup = page.locator('button.button-primary')
        self.signup_btn_login = page.locator('button.btn-blue')


    def signup(self,username,password):
        self.signup_input_username.fill(username)
        self.signup_input_password.fill(password)
        self.signup_btn_signup.click()

    def go_to_home(self):
        self.page.goto(self.base_url)
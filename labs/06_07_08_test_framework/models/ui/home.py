import os

class HomePage:
    def __init__(self, page, base_url=None):
        self.page = page
        self.base_url = base_url or os.getenv("APP_URL", "http://localhost:5173")
        self.login_header_main_title = page.get_by_text('Nackademin Course App')
        self.login_input_username = page.get_by_placeholder('Username')
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_btn_login = page.locator('button.button-primary')
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_signup = page.locator('#signup')


    def navigate(self):
        self.page.goto(self.base_url)
        self.page.wait_for_selector('input[placeholder="Username"]')


    def login(self,username,password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()


    def go_to_signup(self):
        self.login_btn_signup.click()
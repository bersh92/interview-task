from fixture.step import StepHelper
import requests


class ScotiaBank:

    RATES_AND_FEES_BUTTON = "//span[text()='Rates & Fees']"
    VIEW_ALL_BUTTON = "//span[text()='Rates & Fees']/ancestor::li //a[text()='View All']"
    ALLOW_ALL_COOKIES_BUTTON = '#onetrust-accept-btn-handler'
    RATES_AND_FEES_TITLE = 'div[class="title bns--title"]'


    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd

    def open_url(self, url):
        self.wd.get(url)

    def click_view_all_in_rates_and_fees(self):
        self.step.hover_then_click(self.RATES_AND_FEES_BUTTON, self.VIEW_ALL_BUTTON)

    def click_allow_cookies_if_present(self):
        if self.step.specified_element_is_present(self.ALLOW_ALL_COOKIES_BUTTON):
            self.step.click_on_element(self.ALLOW_ALL_COOKIES_BUTTON)

    def rates_and_fees_title(self):
        return self.step.get_element_text(self.RATES_AND_FEES_TITLE).strip()

    def get_url_info(self, url):
        try:
            response = requests.get(url, allow_redirects=True, timeout=10)
            return {
                'status_code': response.status_code,
                'headers': response.headers,
                'url': response.url,
                'content_length': response.headers.get('Content-Length'),
                'content_type': response.headers.get('Content-Type'),
            }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL info: {e}")
            return None

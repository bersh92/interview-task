# 1.Go to https://www.scotiabank.com/ca/en/personal.html
# 2. Hover on Rates&Fees
# 3. Click on View All and verify the URL
# 4. Return the status of the URL using API header

def test_verify_rates_and_fees(app):
    app.scotiaBank.open_url('https://www.scotiabank.com/ca/en/personal.html')
    app.scotiaBank.click_allow_cookies_if_present()
    app.scotiaBank.click_view_all_in_rates_and_fees()
    app.assert_that(app.wd.current_url).is_equal_to('https://www.scotiabank.com/ca/en/personal/rates-prices.html')
    app.assert_that(app.scotiaBank.rates_and_fees_title()).is_equal_to('Rates and fees')

def test_verify_rates_and_fees_response(app):
    response = app.scotiaBank.get_url_info('https://www.scotiabank.com/ca/en/personal/rates-prices.html')
    app.assert_that(response['status_code']).is_equal_to(200)
    app.assert_that(response['content_length']).is_equal_to('26389')
    app.assert_that(response['content_type']).is_equal_to('text/html; charset=UTF-8')
    app.assert_that(response['headers']).contains_key('Content-Type')
    app.assert_that(response['headers']['Content-Type']).is_equal_to('text/html; charset=UTF-8')
    app.assert_that(response['headers']).contains_key('Content-Length')
    app.assert_that(response['headers']['Content-Length']).is_equal_to('26389')
    app.assert_that(response['headers']).contains_key('Strict-Transport-Security')
    app.assert_that(response['headers']['Strict-Transport-Security']).is_equal_to('max-age=31536000 ; includeSubDomains ; preload')
    app.assert_that(response['url']).is_equal_to('https://www.scotiabank.com/ca/en/personal/rates-prices.html')

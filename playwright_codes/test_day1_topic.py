from playwright.sync_api import Page, expect


fmtc_url = "https://fortune-media.onrender.com/"
fmtc_title = "Fortune Media - Premium Outdoor Advertising & Marketing Solutions"


def test_fmtc_home_page_url(page: Page):

    # Navigate to URL
    page.goto(fmtc_url)
    print(f"Navigated to {fmtc_url} successfully")

    # wait for timeout
    page.wait_for_timeout(3000)
    expect(page).to_have_url(fmtc_url)
    print(f"Successfully verified {fmtc_url} in navigated page")

def test_fmtc_home_page_title(page:Page):

    # Navigate to URL
    page.goto(fmtc_url)
    print(f"Navigated to {fmtc_url} successfully")
    page.wait_for_timeout(3000)

    # Verify FMTC page Title
    expect(page).to_have_title(fmtc_title)
    page.wait_for_timeout(5000)

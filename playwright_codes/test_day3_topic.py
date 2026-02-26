import pytest
import re
from playwright.sync_api import Page, expect


fmtc_url = "https://fortune-media.onrender.com/"
fmtc_title = "Fortune Media - Premium Outdoor Advertising & Marketing Solutions"

# test_url = "https://testautomationpractice.blogspot.com/"
test_url = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"
test_title = "Automation Testing Practice: PlaywrightPractice"

@pytest.fixture(scope="function")
def get_fmtc_url(page:Page):
    page.goto(fmtc_url)
    page.wait_for_timeout(3000)
    expect(page).to_have_url(fmtc_url)
    expect(page).to_have_title(fmtc_title)
    yield page

@pytest.fixture(scope="function")
def get_test_url(page:Page):
    page.goto(test_url)
    page.wait_for_timeout(3000)
    expect(page).to_have_url(test_url, timeout=5000)
    expect(page).to_have_title(test_title, timeout=5000)
    yield page


def test_get_by_alt_text(get_fmtc_url):
    page = get_fmtc_url
    expect(page.get_by_alt_text("Fortune Media Team")).to_be_visible()
    print("Fortune Media Team alt_text is visible")
    page.wait_for_timeout(500)

def test_get_by_text(get_fmtc_url):
    page = get_fmtc_url
    expect(page.get_by_text("Trusted by Leading Brands")).to_be_visible()
    print(f"Trusted by Leading Brands text is visible")
    expect(page.get_by_text("Fortune").nth(1)).to_be_visible()
    print(f"Fortune text is visible")
    expect(page.get_by_text("Media").nth(1)).to_be_visible()
    print(f"Media text is visible")

    """Digital Display Innovation
    State-of-the-art LED displays for maximum impact"""
    expect(page.get_by_text("ital Display Innova")).to_be_visible()
    print(f"ital Display Innova text is visible")
    expect(page.get_by_text("State-of-the-art")).to_be_visible()
    print(f"State-of-the-art text is visible")

    # Regular expression logic missing from here
    expect(page.get_by_text(re.compile(r".*creative approach.*$", re.IGNORECASE))).to_be_visible()
    print(f"FMTC website element visibility verified with regex compile")
    page.wait_for_timeout(5000)

def test_get_by_role(get_fmtc_url):
    page = get_fmtc_url
    expect(page.get_by_role("navigation").get_by_role("button", name="About Us")).to_be_visible(timeout=10000)
    print(f"About Us located successfully")
    page.get_by_role("main").get_by_role("button", name="About Us").click()
    print(f"About Us clicked successfully")
    page.wait_for_timeout(10000)

def test_get_by_label(get_test_url):
    page = get_test_url
    expect(page.get_by_label("Email Address:")).to_be_visible()
    print(f"Email Address: label is visible")
    page.get_by_label("Email Address:").fill("ibrahim.sma1990@gmail.com")
    print(f"Email Address: ibrahim.sma1990@gmail.com filled successfully")
    page.wait_for_timeout(5000)

def test_get_by_placeholder(get_test_url):
    page = get_test_url
    page.get_by_placeholder("Enter your full name").fill("Ibrahim Sma")
    page.wait_for_timeout(5000)

def test_get_by_title(get_test_url):
    page = get_test_url
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    expect(page.get_by_title("Tooltip text")).to_have_text("This text has a tooltip")
    page.wait_for_timeout(5000)

def test_get_by_test_id(get_test_url):

    page = get_test_url
    product_name = page.get_by_test_id("product-card-1").get_by_test_id("product-name").inner_text()
    print(f"Product Name: {product_name}")
    product_price = page.get_by_test_id("product-card-1").get_by_test_id("product-price").inner_text()
    print(f"Product Price: {product_price}")
    expect(page.get_by_test_id("product-card-1").get_by_test_id("product-name")).to_have_text("Product A")
    print(f"Product Name: Product A is visible")
    page.wait_for_timeout(5000)

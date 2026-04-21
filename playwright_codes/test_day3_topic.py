import pytest
import re
from playwright.sync_api import Page, expect


def test_css_selectors(page:Page):

    page.goto("https://demowebshop.tricentis.com/")
    logo = page.locator("")


# Pre-requisite for Asynchrouns execution
# install  pytest-asyncio
# command:   pip install pytest-asyncio

from playwright.async_api import async_playwright,Page, expect
import pytest

@pytest.mark.asyncio
async def test_verifyPageUrl_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  #  headed mode
        mypage = await browser.new_page()
        await mypage.goto("http://www.automationpractice.pl/index.php")
        await expect(mypage).to_have_url("http://www.automationpractice.pl/index.php")
        await browser.close()


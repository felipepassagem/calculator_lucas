from playwright.sync_api import sync_playwright
import time


FRONT_URL = "http://127.0.0.1:5500/front/index.html"  # ajuste se precisar


def test_soma_e2e():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(FRONT_URL)
        page.wait_for_load_state("networkidle")

        # 2 + 3 =
        page.click('[data-num="2"]')
        page.click('[data-op="+"]')
        page.click('[data-num="3"]')
        page.click('[data-action="equal"]')

        # 🔥 Espera até o visor conter exatamente "5"
        page.wait_for_function(
            """() => {
                const el = document.querySelector('#display-result');
                return el && el.textContent.trim() === '5';
            }"""
        )

        result_text = page.locator("#display-result").inner_text().strip()
        browser.close()

        assert result_text == "5"

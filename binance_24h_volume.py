import logging


def binance_24h_volume(playwright):
    browser = playwright.chromium.launch(headless=True)
    # Set user_agent so that the script can run in headless mode.
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/88.0.4324.150 Safari/537.36")
    page = context.new_page()

    page.goto('https://www.coingecko.com/en/exchanges/binance')
    volume_selector = 'div:nth-child(1) > span[data-prev-price]'
    volume_element = page.wait_for_selector(volume_selector)
    total_24h_volume_str = volume_element.text_content()
    context.close()
    browser.close()
    logging.info(f"Binance 24h trading volume is: {total_24h_volume_str}")
    return total_24h_volume_str

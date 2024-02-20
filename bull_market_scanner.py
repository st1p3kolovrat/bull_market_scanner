import logging
from datetime import datetime
from assertpy import assert_that
from playwright.sync_api import sync_playwright
from bitcoin_rsi import bitcoin_rsi
from fear_and_greed_index import fear_and_greed_index
from binance_24h_volume import binance_24h_volume
from send_telegram_msg import send_telegram_msg

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def today_time():
    return datetime.now().strftime("%d.%m.%Y")


def main():
    condition_met = False

    # Initial message with date and basic information
    full_message = f"""<b>Daily Bull Market Scanner Report\nDate: {today_time()}</b>\n<b>────────────</b>\n\n"""

    ####################
    #    GREED INDEX   #
    ####################
    greed_index_value = fear_and_greed_index()
    # Append to the message if greed index value is above given value
    if greed_index_value > 80:
        condition_met = True
        greed_message = f"<b>Greed Index: </b>{greed_index_value} ⚠️ - Level High!\n"
        full_message += f"\n{greed_message}\n"
    else:
        pass

    ####################
    #      BTC RSI     #
    ####################
    rsi_value = bitcoin_rsi()
    # Append to the message if RSI value is above given value
    if rsi_value > 90:
        condition_met = True
        rsi_message = f"<b>Bitcoin (1W) RSI: </b>{rsi_value} ⚠️ - Overbought!\n"
        full_message += f"{rsi_message}\n"
    else:
        pass

    ###################################
    #    BINANCE 24h TRADING VOLUME   #
    ###################################
    with sync_playwright() as playwright:
        binance_volume_str = binance_24h_volume(playwright)

    # Extract the numeric part for comparison
    total_volume_int = int(binance_volume_str.replace("$", "").replace(",", ""))

    if total_volume_int > 60000000000:
        condition_met = True
        # make it more readable in format e.g. $55.38 B
        convert_billions = total_volume_int / 1_000_000_000
        total_24h_volume = f"${convert_billions:.2f} B"

        binance_24h_volume_msg = f"<b>Binance 24h Volume: </b>{total_24h_volume} ⚠️ - Attention!\n"
        full_message += f"{binance_24h_volume_msg}\n"
    else:
        pass

    if condition_met:
        telegram_response = send_telegram_msg(full_message)
        assert_that(telegram_response.status_code).is_equal_to(200)
    else:
        logging.info("Message to Telegram was not sent because all indicator conditions are not met")


if __name__ == "__main__":
    main()

import datetime


def generate_message() -> dict:
    current_time = datetime.datetime.now()
    id = f"{current_time.year}{current_time.month}{current_time.day}{current_time.hour}{current_time.minute}{current_time.second}{current_time.microsecond}"
    ticker = "GOOG"
    price_info = 123

    return {
        "id": id,
        "ticker": ticker,
        "price": price_info,
    }

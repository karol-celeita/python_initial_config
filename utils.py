import datetime

def get_timestamp_for_logs() -> str:
    """get_timestamp_for_logs
    
    Esta funcion se encarga de capturar la fecha actual y retornarla en un formato:
    YYYY-MM-DD HH:mm:ss

    Returns:
        str: YYYY-MM-DD HH:mm:ss
    """
    today = datetime.datetime.now()
    time_now = f"{today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second}"
    return str(time_now)
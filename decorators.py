import time
from config import RATE_LIMIT




def rate_limit(func):
    async def wrapper(context, user_id, text):
        current_time = time.time()
        last_message_time = context.user_data.get('last_message_time', 0)

        if current_time - last_message_time < RATE_LIMIT:
            return "Слишком много запросов. Подождите пару секунд."

        context.user_data['last_message_time'] = current_time

        return await func(context, user_id, text)
    return wrapper


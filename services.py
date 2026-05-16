from repository import save_message
from ai import get_ai_response
from repository import get_or_create_user


async def process_chat(message, db):
    user = get_or_create_user(message.user_id, db)
    messages = [
        {"role": "user", "content": message.text}
    ]
    save_message(message.user_id, "user", message.text, db)
    answer = await get_ai_response(messages)
    save_message(message.user_id, "assistant", answer, db)
    return answer
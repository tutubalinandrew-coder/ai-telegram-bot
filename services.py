from repository import get_last_messages, save_message
from ai import get_ai_response
from repository import get_or_create_user


async def process_chat(message, db):
    user = get_or_create_user(message.user_id, db)
    history = get_last_messages(message.user_id, 20, db)
    history.reverse()
    messages = []

    for role, text in history:
        messages.append(
        {"role": role, "content": text}
        )  
    messages.append({"role": "user", "content": message.text})
    
    save_message(message.user_id, "user", message.text, db)
    answer = await get_ai_response(messages)
    save_message(message.user_id, "assistant", answer, db)
    return answer
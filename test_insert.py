from postgres_database import save_message

save_message(
    user_id=123,
    role='user',
    message='Hello PostreSQL'
)

print('Message saved')
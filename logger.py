from datetime import datetime

def log_message(user_text, ai_answer):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(
            f"[{current_time}]\n"
            f"USER: {user_text}\n"
            f"AI: {ai_answer}\n"
            f"---\n"
        )
        print(f"USER: {user_text}")
    

def log_error(error):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(
            f"[{current_time}]\n"
            f"ERROR: {error}\n"
            f"---\n"
        )
        print(f"ERROR: {error}")



import logging

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s'
        )
logger = logging.getLogger(__name__)

def log_message(user_text, ai_answer):
    logger.info(f"USER: {user_text}\nASSISTANT: {ai_answer}")
    
    

def log_error(error):
    logger.error(error)



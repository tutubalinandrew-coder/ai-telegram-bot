from config import ERROR_MESSAGE, OPENAI_MODEL
from openai import AsyncOpenAI
client = AsyncOpenAI()

async def get_ai_response(messages):
    try:
        response = await client.chat.completions.create( 
            model = OPENAI_MODEL,
            messages=messages,
        )
        ai_answer = response.choices[0].message.content
        print(ai_answer)
        return ai_answer
    except Exception as e:
        print(f"OpenAI error: {e}")
        return ERROR_MESSAGE
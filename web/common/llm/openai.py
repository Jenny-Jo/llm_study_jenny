import enum
from openai import OpenAI
import time

class OPENAI_LLMs(enum.Enum):
  gpt_4o_mini = (enum.auto(), "gpt-4o-mini") 
  gpt_4o = (enum.auto(), "gpt-4o") 

def ClientOpenAI(
    model_name,
    messages,
    stream=True
):
    
    client = OpenAI()
    response = client.chat.completions.create(
        model=OPENAI_LLMs[model_name].value[1],
        messages=messages,
        stream=stream
    )
    for token in response:
        if token.choices[0].delta.content is not None:
            yield token.choices[0].delta.content
            time.sleep(0.05)

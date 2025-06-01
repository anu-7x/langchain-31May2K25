from const import OPEN_AI_API_KEY

from langchain_openai import OpenAI

llm = OpenAI(
  api_key=OPEN_AI_API_KEY,
)
name: str = llm.invoke("I need to open a startup in the IT field. Can you give me a name for it?")
print(f"Name of the startup: {name}")


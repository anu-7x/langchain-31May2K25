from const import OPEN_AI_API_KEY
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

llm = OpenAI(
  name="gpt-4.1-nano",
  api_key=OPEN_AI_API_KEY,
)
#
prompt = PromptTemplate.from_template("How to say {input} in {output_language}:\n")
chain = prompt | llm 
text_data = chain.invoke(
    {
        "output_language": "German",
        "input": "I love programming.",
    }
)
#
# print the output
print(f"Output: {text_data}")
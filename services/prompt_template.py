from const import OPEN_AI_API_KEY
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

# this is the template for the prompt, So by using the variable fields, you can change the prompt dynamically!
# ( here we using the field variable to change the prompt dynamically.)
prompt_company_name = PromptTemplate(
    input_variables=["field"],
    template="I need to open a startup in the {field} field. Can you give me a name for it? Just give me only 1 name.",
)

prompt_company_name.format(field="software development") 
print(prompt_company_name.format(field="software development"))

llm = OpenAI(
  api_key=OPEN_AI_API_KEY,
)
name: str | None = None
name = llm.invoke(prompt_company_name.format(field="software development"))
print(f"Name of the startup: {name}")


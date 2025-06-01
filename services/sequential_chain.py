from const import OPEN_AI_API_KEY
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain

##-# Define the LLM
llm = OpenAI(
  name="gpt-4.1-nano",
  api_key=OPEN_AI_API_KEY,
)
##-# Define the prompt templates & chains
prompt_restaurant_name = PromptTemplate(
  import_variables=["cuisine"],
  template="I need to open a restaurant that serves {cuisine} food. Can you give me a name for it? Just give me only 1 name.",
)
name_chain = LLMChain(llm=llm, prompt=prompt_restaurant_name, output_key="restaurant_name")

prompt_template_items = PromptTemplate(
  input_variables=["restaurant_name"],
  template="What are the top 2 items on the menu for a restaurant named {restaurant_name}?",
)
items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
#
seq_chain = SequentialChain(
  chains=[name_chain, items_chain],
  input_variables=["cuisine"],
  output_variables=["restaurant_name", "menu_items"],
)
chain_data = seq_chain.invoke({"cuisine": "Italian"})
print(f"Response: {chain_data}")

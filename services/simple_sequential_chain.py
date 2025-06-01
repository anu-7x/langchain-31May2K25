from const import OPEN_AI_API_KEY
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain

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
name_chain = LLMChain(llm=llm, prompt=prompt_restaurant_name)

prompt_template_items = PromptTemplate(
  input_variables=["restaurant_name"],
  template="What are the top 2 items on the menu for a restaurant named {restaurant_name}?",
)
items_chain = LLMChain(llm=llm, prompt=prompt_template_items)
#
##-# Build the sequential chain & run it
seq_chain = SimpleSequentialChain(chains=[name_chain, items_chain])
# response = seq_chain.invoke(input={"cuisine": "Italian"}) -> Invalid Because,
# SimpleSequentialChain is designed to accept a single string input under the default key "input", not a dictionary of inputs with named variables.
# We need to go with `SequentialChain` if we want to use multiple inputs. :)
response = seq_chain.invoke({"input": "Italian"})
print(f"Response: {response}")

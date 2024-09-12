from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openai_api_key

import os
os.environ['OPENAI_API_KEY'] = openai_api_key

llm = OpenAI(temperature=0.7)

def get_country_and_cities(continent):
    # Chain 1: Continent
    prompt_template_name = PromptTemplate(
        input_variables = ['continent'],
        template = "Give name of a random country from " + continent + ". Only give one name without any explanations."
    )

    continent_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="country")

    # Chain 2: Cities
    prompt_template_name = PromptTemplate(
        input_variables = ['country'],
        template = "List five cities {country}. Return output as comma seperated list"
    )

    cities_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="cities")

    chain = SequentialChain(
        chains = [continent_chain, cities_chain],
        input_variables = ['continent'],
        output_variables = ['country', 'cities']
    )

    response = chain.invoke({'continent': 'continent'})
    return response

if __name__ == "__main__":
    print(get_country_and_cities('Europe'))
    # Example Output: {'country': 'France', 'cities': 'Paris, Marseille, Lyon, Toulouse, Nice'}

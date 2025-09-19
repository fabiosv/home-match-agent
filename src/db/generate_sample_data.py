from ..provider import LLMProvider
from langchain.output_parsers import PydanticOutputParser
from .models import RealEstateListingsResult
from langchain.prompts import PromptTemplate


def create_real_estate_listings(llm: LLMProvider, num_listings=2):
    """ Generate real estate listings using an AI model via the ask_ai function.

    Args:
        ask_ai (function): Function to send prompts to the AI model.
        num_listings (int): Number of unique listings to generate.
    Returns:
        list: A list of dictionaries containing real estate listings.
    """
    context = "You are a helpful assistant that generates realistic real estate listings. The listings should include various details about the property and neighborhood and should not be repetitive."
    question = f"Generate a total of {num_listings} real estate listings."
    examples = [{
        "neighborhood": "Green Oaks",
        "price": "$800,000",
        "bedrooms": 3,
        "bathrooms": 2,
        "house_size": "2,000 sqft",
        "description": "Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.",
        "neighborhood_description": "Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze."
    }]

    parser = PydanticOutputParser(pydantic_object=RealEstateListingsResult)
    prompt_template = PromptTemplate(
        template="{context}\n{question}\n{format_instructions}\nFollow some examples(but do not copy this example content):\n{examples}",
        input_variables=["context", "question", "format_instructions"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        },
    ).format(context=context, question=question, examples=examples)

    print('===== Prompt =====')
    print(prompt_template)

    output = []
    while len(output) < num_listings:
        response = llm.ask(prompt_template)
        print(f"Response: {response}")
        data = parser.parse(response).dict().get('results', [])
        output.extend(data)

    return output

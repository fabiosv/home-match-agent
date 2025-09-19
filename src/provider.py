from .configs import provider_configs
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


class LLMProvider:
    """ A class to handle interactions with different LLM providers. """

    def __init__(self, provider='OPEN_AI', extra_configs={}):
        """ Initialize the LLMProvider with the specified provider and configurations. """
        self.configs = provider_configs(provider)
        self.client = ChatOpenAI(**self.configs, **extra_configs)

    def ask(self, prompt, system_prompt=None):
        """ Send a prompt to the LLM and return the response. """
        messages = [
            SystemMessage(content=system_prompt or "You are a helpful assistant."),
            HumanMessage(content=prompt)
        ]

        response = self.client(messages)

        return response.content

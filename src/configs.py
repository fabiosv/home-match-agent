from os import getenv


def provider_configs(provider=None):
    """ Return the configuration for the specified provider. """
    OPENAI_API_KEY = getenv("OPENAI_API_KEY", "your-openai-api-key")
    OPENAI_API_BASE = getenv("OPENAI_API_BASE", "https://openai.vocareum.com/v1")
    PROVIDER = provider or getenv("DEFAULT_PROVIDER", "OPEN_AI")

    default_configs = {
        'LM_STUDIO': {
            'base_url': 'http://127.0.0.1:1234/v1',
            'api_key': 'voc-00000000000000000000000000000000abcd.12345678'
        },
        'OPEN_AI': {
            'base_url': OPENAI_API_BASE,
            'api_key': OPENAI_API_KEY
        }
    }
    models = {
        'LM_STUDIO': 'airoboros-gpt-3.5-turbo-100k-7b',
        'OPEN_AI': 'gpt-3.5-turbo',
    }

    return {
        **default_configs.get(PROVIDER, default_configs['LM_STUDIO']),
        'model_name': models.get(PROVIDER, models['LM_STUDIO'])
    }

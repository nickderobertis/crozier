

import typing

ModelProviderType = typing.Union[
    typing.Literal[
        "anthropic",
        "bedrock",
        "cerebras",
        "chutes",
        "cohere",
        "deepseek",
        "gemini",
        "github",
        "groq",
        "watsonx",
        "jan",
        "mistral",
        "moonshot",
        "nvidia",
        "ollama",
        "openai",
        "openrouter",
        "perplexity",
        "together",
        "voyage",
        "rits",
        "other",
    ],
    typing.Any,
]

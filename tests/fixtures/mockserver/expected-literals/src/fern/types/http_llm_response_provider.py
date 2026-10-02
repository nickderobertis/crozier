

import typing

HttpLlmResponseProvider = typing.Union[
    typing.Literal[
        "ANTHROPIC",
        "OPENAI",
        "OPENAI_RESPONSES",
        "GEMINI",
        "BEDROCK",
        "AZURE_OPENAI",
        "OLLAMA",
        "COHERE",
        "VOYAGE",
        "MISTRAL",
        "XAI",
        "DEEPSEEK",
        "GROQ",
        "OPENROUTER",
        "ORCAROUTER",
    ],
    typing.Any,
]

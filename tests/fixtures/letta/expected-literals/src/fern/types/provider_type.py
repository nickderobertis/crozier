

import typing

ProviderType = typing.Union[
    typing.Literal[
        "anthropic",
        "azure",
        "bedrock",
        "cerebras",
        "chatgpt_oauth",
        "deepseek",
        "google_ai",
        "google_vertex",
        "groq",
        "hugging-face",
        "letta",
        "lmstudio_openai",
        "mistral",
        "ollama",
        "openai",
        "together",
        "vllm",
        "sglang",
        "xai",
        "zai",
    ],
    typing.Any,
]

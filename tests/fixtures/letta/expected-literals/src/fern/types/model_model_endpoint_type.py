

import typing

ModelModelEndpointType = typing.Union[
    typing.Literal[
        "openai",
        "anthropic",
        "google_ai",
        "google_vertex",
        "azure",
        "groq",
        "ollama",
        "webui",
        "webui-legacy",
        "lmstudio",
        "lmstudio-legacy",
        "lmstudio-chatcompletions",
        "llamacpp",
        "koboldcpp",
        "vllm",
        "hugging-face",
        "mistral",
        "together",
        "bedrock",
        "deepseek",
        "xai",
        "zai",
        "chatgpt_oauth",
    ],
    typing.Any,
]

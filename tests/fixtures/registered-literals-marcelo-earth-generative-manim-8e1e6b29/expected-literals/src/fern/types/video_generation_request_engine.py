

import typing

VideoGenerationRequestEngine = typing.Union[
    typing.Literal["openai", "anthropic", "featherless", "gemini", "litellm", "moonshot"], typing.Any
]

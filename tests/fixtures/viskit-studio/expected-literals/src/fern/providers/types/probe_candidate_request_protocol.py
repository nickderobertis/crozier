

import typing

ProbeCandidateRequestProtocol = typing.Union[
    typing.Literal["openai_compatible", "anthropic_compatible", "image_generation"], typing.Any
]

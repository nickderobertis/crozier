

import typing

from .prompt_one import PromptOne
from .prompt_zero import PromptZero

Prompt = typing.Union[PromptZero, PromptOne]

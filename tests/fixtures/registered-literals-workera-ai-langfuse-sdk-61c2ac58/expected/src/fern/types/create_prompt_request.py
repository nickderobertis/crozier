

import typing

from .create_prompt_request_one import CreatePromptRequestOne
from .create_prompt_request_zero import CreatePromptRequestZero

CreatePromptRequest = typing.Union[CreatePromptRequestZero, CreatePromptRequestOne]

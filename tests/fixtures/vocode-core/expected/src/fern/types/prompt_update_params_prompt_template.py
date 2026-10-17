

import typing

from .prompt_template import PromptTemplate
from .undefined import Undefined

PromptUpdateParamsPromptTemplate = typing.Union[str, PromptTemplate, Undefined]

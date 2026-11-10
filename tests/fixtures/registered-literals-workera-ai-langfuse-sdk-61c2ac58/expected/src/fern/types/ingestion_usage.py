

import typing

from .open_ai_usage import OpenAiUsage
from .usage import Usage

IngestionUsage = typing.Union[Usage, OpenAiUsage]

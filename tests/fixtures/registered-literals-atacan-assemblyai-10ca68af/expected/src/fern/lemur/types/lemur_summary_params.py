

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from .lemur_base_params import LemurBaseParams


class LemurSummaryParams(LemurBaseParams):
    answer_format: typing.Optional[str] = pydantic.Field(default=None)
    """
    How you want the summary to be returned. This can be any text. Examples: "TLDR", "bullet points"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

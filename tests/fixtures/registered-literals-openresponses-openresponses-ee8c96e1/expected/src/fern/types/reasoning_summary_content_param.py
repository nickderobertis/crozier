

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reasoning_summary_content_param_type import ReasoningSummaryContentParamType


class ReasoningSummaryContentParam(UniversalBaseModel):
    type: ReasoningSummaryContentParamType = pydantic.Field()
    """
    The content type. Always `summary_text`.
    """

    text: str = pydantic.Field()
    """
    The reasoning summary text.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reasoning_item_param_type import ReasoningItemParamType
from .reasoning_summary_content_param import ReasoningSummaryContentParam


class ReasoningItemParam(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of this reasoning item.
    """

    type: ReasoningItemParamType = pydantic.Field()
    """
    The item type. Always `reasoning`.
    """

    summary: typing.List[ReasoningSummaryContentParam] = pydantic.Field()
    """
    Reasoning summary content associated with this item.
    """

    content: typing.Optional[typing.Any] = None
    encrypted_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    An encrypted representation of the reasoning content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

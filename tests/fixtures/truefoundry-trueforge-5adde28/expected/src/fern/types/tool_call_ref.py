

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ToolCallRef(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Tool call id awaiting action.
    """

    source_event_id: str = pydantic.Field()
    """
    Event id of the model.message that requested the tool call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

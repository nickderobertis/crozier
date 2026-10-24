

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_message_response_object import CreateMessageResponseObject
from .create_single_message_response import CreateSingleMessageResponse


class CreateMessageResponse(UniversalBaseModel):
    object: CreateMessageResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[CreateSingleMessageResponse] = pydantic.Field()
    """
    List of messages and their statuses
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommonMessage(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    Message sent by user
    """

    channel_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="channelId"),
        pydantic.Field(alias="channelId", description="Id of channel to which message was sent"),
    ]
    """
    Id of channel to which message was sent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueueMessage(UniversalBaseModel):
    """
    A Queue Message
    """

    content_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="contentType")] = (
        pydantic.Field(default=None)
    )
    """
    Content-type of data associated with QueueMessage.
    """

    create_date: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="createDate")] = pydantic.Field(
        default=None
    )
    """
    Date that message was received by system.
    """

    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    Embedded JSON to be sent with Queue Message.
    """

    href: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of data associated with Queue Message (if not embedded JSON)
    """

    message_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="messageId")] = pydantic.Field(
        default=None
    )
    """
    UUID of Message Data associated with this Queue Message
    """

    queue_message_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="queueMessageId")] = (
        pydantic.Field(default=None)
    )
    """
    UUID of Queue Message in local region.
    """

    queue_name: typing_extensions.Annotated[str, FieldMetadata(alias="queueName")] = pydantic.Field()
    """
    Name of Queue for message.
    """

    receiving_region: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="receivingRegion")] = (
        pydantic.Field(default=None)
    )
    """
    Regions to which message will be sent
    """

    sending_region: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="sendingRegion")] = (
        pydantic.Field(default=None)
    )
    """
    Region from which was sent
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_array import MessageArray
from .service import Service


class ServiceView(UniversalBaseModel):
    """
    Aggregate bean for grouping a Service an its messages pairs
    """

    messages_map: typing_extensions.Annotated[
        typing.Dict[str, MessageArray],
        FieldMetadata(alias="messagesMap"),
        pydantic.Field(
            alias="messagesMap",
            description="Map of messages for this Service. Keys are operation name, values are array of messages for this operation",
        ),
    ]
    """
    Map of messages for this Service. Keys are operation name, values are array of messages for this operation
    """

    service: Service = pydantic.Field()
    """
    Wrapped service description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

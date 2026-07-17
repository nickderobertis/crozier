

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .queue import Queue
from .queue_message import QueueMessage


class ApiResponse(UniversalBaseModel):
    """
    Response returned by most Queue API calls.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Count of Queues or QueueMessages returned by the call.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Informative message intended for client.
    """

    queue_messages: typing_extensions.Annotated[
        typing.Optional[typing.List[QueueMessage]],
        FieldMetadata(alias="queueMessages"),
        pydantic.Field(
            alias="queueMessages", description="Queues Messages returned by the call, or empty if not applicable."
        ),
    ] = None
    """
    Queues Messages returned by the call, or empty if not applicable.
    """

    queues: typing.Optional[typing.List[Queue]] = pydantic.Field(default=None)
    """
    Queues returned but the call, or empty if not applicable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

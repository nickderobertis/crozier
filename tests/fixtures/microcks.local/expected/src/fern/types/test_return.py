

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .event_message import EventMessage
from .request import Request
from .response import Response


class TestReturn(UniversalBaseModel):
    """
    TestReturn is used for wrapping the return code of a test step execution
    """

    code: int = pydantic.Field()
    """
    Return code for test (0 means Success, 1 means Failure)
    """

    elapsed_time: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="elapsedTime"),
        pydantic.Field(alias="elapsedTime", description="Elapsed time in milliseconds"),
    ]
    """
    Elapsed time in milliseconds
    """

    event_message: typing_extensions.Annotated[
        typing.Optional[EventMessage],
        FieldMetadata(alias="eventMessage"),
        pydantic.Field(alias="eventMessage", description="Event Message received for this test"),
    ] = None
    """
    Event Message received for this test
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message if any
    """

    request: typing.Optional[Request] = pydantic.Field(default=None)
    """
    Request sent for this test
    """

    response: typing.Optional[Response] = pydantic.Field(default=None)
    """
    Response returned for this test
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

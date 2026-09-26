

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EventsRemediationsGetResponseData(UniversalBaseModel):
    session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sessionId"), pydantic.Field(alias="sessionId", description="Session ID")
    ]
    """
    Session ID
    """

    tool_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="toolName"), pydantic.Field(alias="toolName", description="Tool that owns the session")
    ]
    """
    Tool that owns the session
    """

    status: str = pydantic.Field()
    """
    Current session status
    """

    issue: str = pydantic.Field()
    """
    Issue being investigated
    """

    timestamp: str = pydantic.Field()
    """
    Event timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

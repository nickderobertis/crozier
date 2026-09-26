

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AgentCapabilities(UniversalBaseModel):
    """
    Describes which protocol features the agent supports. In addition to the standard capabilities (prefixed with ap.), implementations can declare custom capabilities, named in reverse domain notation (eg. com.example.some.capability).
    """

    ap_io_messages: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ap.io.messages"),
        pydantic.Field(
            alias="ap.io.messages",
            description="Whether the agent supports Messages as input/output/state. If true, the agent uses the `messages` key in threads/runs endpoints.",
        ),
    ] = None
    """
    Whether the agent supports Messages as input/output/state. If true, the agent uses the `messages` key in threads/runs endpoints.
    """

    ap_io_streaming: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="ap.io.streaming"),
        pydantic.Field(alias="ap.io.streaming", description="Whether the agent supports streaming output."),
    ] = None
    """
    Whether the agent supports streaming output.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

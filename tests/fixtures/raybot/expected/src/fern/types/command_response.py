

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .command_inputs import CommandInputs
from .command_outputs import CommandOutputs
from .command_source import CommandSource
from .command_status import CommandStatus
from .command_type import CommandType


class CommandResponse(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    The id of the command
    """

    type: CommandType = pydantic.Field()
    """
    The type of command
    """

    status: CommandStatus = pydantic.Field()
    """
    The status of the command
    """

    source: CommandSource = pydantic.Field()
    """
    The source of the command
    """

    inputs: CommandInputs = pydantic.Field()
    """
    The inputs of the command
    """

    outputs: CommandOutputs = pydantic.Field()
    """
    The outputs of the command
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error of the command
    """

    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="The start date of the command"),
    ] = None
    """
    The start date of the command
    """

    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completedAt"),
        pydantic.Field(alias="completedAt", description="The completion date of the command"),
    ] = None
    """
    The completion date of the command
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The creation date of the command"),
    ]
    """
    The creation date of the command
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The update date of the command"),
    ]
    """
    The update date of the command
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

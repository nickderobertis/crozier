

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BuildSystemSharedDtoAgentStatus(UniversalBaseModel):
    """
    A DTO for an IAgentStatus
    """

    last_status_update: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastStatusUpdate"),
        pydantic.Field(
            alias="LastStatusUpdate", description="ReadOnly. The UTC date and time of the last status update"
        ),
    ] = None
    """
    ReadOnly. The UTC date and time of the last status update
    """

    online: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Online"),
        pydantic.Field(alias="Online", description="Indicates if the agent is online"),
    ]
    """
    Indicates if the agent is online
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

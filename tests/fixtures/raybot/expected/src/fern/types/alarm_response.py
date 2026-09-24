

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alarm_data import AlarmData
from .alarm_type import AlarmType


class AlarmResponse(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    The id of the alarm
    """

    type: AlarmType = pydantic.Field()
    """
    The type of alarm
    """

    message: str = pydantic.Field()
    """
    The alarm message
    """

    data: AlarmData = pydantic.Field()
    """
    The data of the alarm
    """

    activated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="activatedAt"),
        pydantic.Field(alias="activatedAt", description="The activation date of the alarm"),
    ]
    """
    The activation date of the alarm
    """

    deactivated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deactivatedAt"),
        pydantic.Field(alias="deactivatedAt", description="The deactivation date of the alarm"),
    ] = None
    """
    The deactivation date of the alarm
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

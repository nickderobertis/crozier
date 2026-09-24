

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alarm_response import AlarmResponse


class AlarmsListResponse(UniversalBaseModel):
    total_items: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalItems"),
        pydantic.Field(alias="totalItems", description="The total number of alarms"),
    ]
    """
    The total number of alarms
    """

    items: typing.List[AlarmResponse] = pydantic.Field()
    """
    The list of alarms
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

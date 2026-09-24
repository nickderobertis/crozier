

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DistanceSensorState(UniversalBaseModel):
    front_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="frontDistance"),
        pydantic.Field(alias="frontDistance", description="The front distance of the distance sensor"),
    ]
    """
    The front distance of the distance sensor
    """

    back_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="backDistance"),
        pydantic.Field(alias="backDistance", description="The back distance of the distance sensor"),
    ]
    """
    The back distance of the distance sensor
    """

    down_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="downDistance"),
        pydantic.Field(alias="downDistance", description="The down distance of the distance sensor"),
    ]
    """
    The down distance of the distance sensor
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the distance sensor"),
    ]
    """
    The updated at time of the distance sensor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

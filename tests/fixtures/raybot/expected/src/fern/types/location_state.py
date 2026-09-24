

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LocationState(UniversalBaseModel):
    current_location: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="currentLocation"),
        pydantic.Field(alias="currentLocation", description="The current location of the robot"),
    ]
    """
    The current location of the robot
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The updated at time of the location"),
    ]
    """
    The updated at time of the location
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_location import UserLocation


class ExpectedUeBehavior(UniversalBaseModel):
    exp_move_trajectory: typing_extensions.Annotated[
        typing.List[UserLocation], FieldMetadata(alias="expMoveTrajectory"), pydantic.Field(alias="expMoveTrajectory")
    ]
    validity_time: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="validityTime"), pydantic.Field(alias="validityTime")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obstacle_tracking import ObstacleTracking


class CargoLowerConfig(UniversalBaseModel):
    stable_read_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="stableReadCount"),
        pydantic.Field(
            alias="stableReadCount",
            description="The number of stable reads required to consider the lower position reached",
        ),
    ]
    """
    The number of stable reads required to consider the lower position reached
    """

    bottom_obstacle_tracking: typing_extensions.Annotated[
        ObstacleTracking, FieldMetadata(alias="bottomObstacleTracking"), pydantic.Field(alias="bottomObstacleTracking")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

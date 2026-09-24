

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BottomObstacleTracking(UniversalBaseModel):
    enter_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="enterDistance"),
        pydantic.Field(alias="enterDistance", description="Start detecting obstacle when distance is below this value"),
    ]
    """
    Start detecting obstacle when distance is below this value
    """

    exit_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="exitDistance"),
        pydantic.Field(alias="exitDistance", description="Stop detecting obstacle when distance is above this value"),
    ]
    """
    Stop detecting obstacle when distance is above this value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ObstacleTracking(UniversalBaseModel):
    enter_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="enterDistance"),
        pydantic.Field(alias="enterDistance", description="The distance to consider the obstacle present (cm)"),
    ]
    """
    The distance to consider the obstacle present (cm)
    """

    exit_distance: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="exitDistance"),
        pydantic.Field(alias="exitDistance", description="The distance to consider the obstacle cleared (cm)"),
    ]
    """
    The distance to consider the obstacle cleared (cm)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

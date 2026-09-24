

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TripKinetic(UniversalBaseModel):
    """
    Expresses the max and average vehicle speed during this trip.
    """

    avg_speed: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="avgSpeed"), pydantic.Field(alias="avgSpeed")
    ] = None
    max_speed: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxSpeed"), pydantic.Field(alias="maxSpeed")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

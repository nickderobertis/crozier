

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preconditioning_air_conditioning import PreconditioningAirConditioning


class Preconditioning(UniversalBaseModel):
    """
    Preconditioning the vehicle for driver and passenger.
    """

    air_conditioning: typing_extensions.Annotated[
        typing.Optional[PreconditioningAirConditioning],
        FieldMetadata(alias="airConditioning"),
        pydantic.Field(alias="airConditioning"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_preconditioning_air_conditioning import RemotePreconditioningAirConditioning


class RemotePreconditioning(UniversalBaseModel):
    """
    Remote preconditioning the vehicle.
    """

    air_conditioning: typing_extensions.Annotated[
        RemotePreconditioningAirConditioning,
        FieldMetadata(alias="airConditioning"),
        pydantic.Field(alias="airConditioning", description="At least one of the parameters must be provided."),
    ]
    """
    At least one of the parameters must be provided.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

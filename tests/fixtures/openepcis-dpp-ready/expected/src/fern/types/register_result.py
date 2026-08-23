

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RegisterResult(UniversalBaseModel):
    """
    Result of RegisterProductDPP (EN 18222 clause 5.2).
    """

    registration_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="registrationId"),
        pydantic.Field(alias="registrationId", description="Unique registration identifier issued by the registry."),
    ]
    """
    Unique registration identifier issued by the registry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

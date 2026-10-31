

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MaxMisLocation(UniversalBaseModel):
    d_i: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="dI"), pydantic.Field(alias="dI")] = (
        None
    )
    d_j: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="dJ"), pydantic.Field(alias="dJ")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

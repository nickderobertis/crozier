

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CapabilityPrice(UniversalBaseModel):
    mode: typing.Optional[str] = None
    currency: typing.Optional[str] = None
    minimum_minor: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minimumMinor"), pydantic.Field(alias="minimumMinor")
    ] = None
    maximum_minor: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maximumMinor"), pydantic.Field(alias="maximumMinor")
    ] = None
    unit: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

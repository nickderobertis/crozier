

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MediaType(UniversalBaseModel):
    charset: typing.Optional[str] = None
    concrete: typing.Optional[bool] = None
    parameters: typing.Optional[typing.Dict[str, str]] = None
    quality_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="qualityValue"), pydantic.Field(alias="qualityValue")
    ] = None
    subtype: typing.Optional[str] = None
    subtype_suffix: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="subtypeSuffix"), pydantic.Field(alias="subtypeSuffix")
    ] = None
    type: typing.Optional[str] = None
    wildcard_subtype: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="wildcardSubtype"), pydantic.Field(alias="wildcardSubtype")
    ] = None
    wildcard_type: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="wildcardType"), pydantic.Field(alias="wildcardType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

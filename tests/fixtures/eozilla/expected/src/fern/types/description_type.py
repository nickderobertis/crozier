

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .description_type_additional_parameters import DescriptionTypeAdditionalParameters
from .metadata import Metadata


class DescriptionType(UniversalBaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    keywords: typing.Optional[typing.List[str]] = None
    metadata: typing.Optional[typing.List[Metadata]] = None
    additional_parameters: typing_extensions.Annotated[
        typing.Optional[DescriptionTypeAdditionalParameters],
        FieldMetadata(alias="additionalParameters"),
        pydantic.Field(alias="additionalParameters"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

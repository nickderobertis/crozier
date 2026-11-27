

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .manifest_array_config_element_definition_item import ManifestArrayConfigElementDefinitionItem
from .manifest_array_config_type import ManifestArrayConfigType


class ManifestArrayConfig(UniversalBaseModel):
    default_element_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="defaultElementName"), pydantic.Field(alias="defaultElementName")
    ] = None
    description: typing.Optional[str] = None
    element_definition: typing_extensions.Annotated[
        typing.List[ManifestArrayConfigElementDefinitionItem],
        FieldMetadata(alias="elementDefinition"),
        pydantic.Field(alias="elementDefinition"),
    ]
    max_elements: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxElements"), pydantic.Field(alias="maxElements")
    ] = None
    min_elements: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minElements"), pydantic.Field(alias="minElements")
    ] = None
    name: typing.Optional[str] = None
    type: ManifestArrayConfigType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

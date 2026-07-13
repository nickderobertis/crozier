

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .content_models_content_type_default_value import ContentModelsContentTypeDefaultValue


class ContentModelsContentTypeProperty(UniversalBaseModel):
    attributes: typing.Optional[typing.Dict[str, str]] = None
    bind_to_property: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="bindToProperty")] = None
    bound_regex: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="boundRegex")] = None
    child_properties: typing_extensions.Annotated[
        typing.Optional[typing.List["ContentModelsContentTypeProperty"]], FieldMetadata(alias="childProperties")
    ] = None
    content_type_allowed: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentTypeAllowed")
    ] = None
    datatype: typing.Optional[int] = None
    default_values: typing_extensions.Annotated[
        typing.Optional[typing.List[ContentModelsContentTypeDefaultValue]], FieldMetadata(alias="defaultValues")
    ] = None
    enabled: typing.Optional[bool] = None
    entitytype: typing.Optional[str] = None
    fallback: typing.Optional[bool] = None
    is_combo: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isCombo")] = None
    is_external_allowed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isExternalAllowed")
    ] = None
    is_image: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isImage")] = None
    is_title: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isTitle")] = None
    is_video: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isVideo")] = None
    legal_content_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="legalContentTypes")
    ] = None
    localizable: typing.Optional[bool] = None
    max_byte_length: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxByteLength")] = None
    max_file_size: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxFileSize")] = None
    max_height: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxHeight")] = None
    max_length: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxLength")] = None
    max_width: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxWidth")] = None
    min_height: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="minHeight")] = None
    min_width: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="minWidth")] = None
    name: typing.Optional[str] = None
    order: typing.Optional[int] = None
    property_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="propertyDescription")
    ] = None
    property_section: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="propertySection")] = None
    readable_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="readableName")] = None
    regexp: typing.Optional[str] = None
    representation_selection: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="representationSelection")
    ] = None
    representation_validation_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="representationValidationString")
    ] = None
    required: typing.Optional[bool] = None
    root_property_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="rootPropertyName")] = (
        None
    )
    rss_attribute: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="rssAttribute")] = None
    suppress_property: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="suppressProperty")] = (
        None
    )
    validate_as: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="validateAs")] = None
    value: typing.Optional[str] = None
    visible: typing.Optional[bool] = None
    visible_dependency: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="visibleDependency")] = (
        None
    )
    visible_on: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="visibleOn")] = None
    weight: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ContentModelsContentTypeProperty)

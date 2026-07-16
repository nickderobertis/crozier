

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .content_models_content_preview import ContentModelsContentPreview
from .content_models_content_type_property_section import ContentModelsContentTypePropertySection
from .content_models_tag_metadata_definition import ContentModelsTagMetadataDefinition
from .content_models_tag_metadata_item import ContentModelsTagMetadataItem


class ContentModelsContentTypeDescription(UniversalBaseModel):
    allow_comments: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowComments"), pydantic.Field(alias="allowComments")
    ] = None
    auto_english_property_fallback: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoEnglishPropertyFallback"),
        pydantic.Field(alias="autoEnglishPropertyFallback"),
    ] = None
    bind_identifier_to_property: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bindIdentifierToProperty"),
        pydantic.Field(alias="bindIdentifierToProperty"),
    ] = None
    bound_regex: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="boundRegex"), pydantic.Field(alias="boundRegex")
    ] = None
    bulk_uploadable: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="bulkUploadable"), pydantic.Field(alias="bulkUploadable")
    ] = None
    c_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cType"), pydantic.Field(alias="cType")
    ] = None
    content_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentDescription"), pydantic.Field(alias="contentDescription")
    ] = None
    force_identifier_binding: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="forceIdentifierBinding"),
        pydantic.Field(alias="forceIdentifierBinding"),
    ] = None
    name: typing.Optional[str] = None
    preview_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="previewImage"), pydantic.Field(alias="previewImage")
    ] = None
    previews: typing.Optional[typing.List[ContentModelsContentPreview]] = None
    priority: typing.Optional[int] = None
    properties: typing.Optional[typing.List["ContentModelsContentTypeProperty"]] = None
    property_sections: typing_extensions.Annotated[
        typing.Optional[typing.List[ContentModelsContentTypePropertySection]],
        FieldMetadata(alias="propertySections"),
        pydantic.Field(alias="propertySections"),
    ] = None
    reminder: typing.Optional[str] = None
    show_in_content_editor: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showInContentEditor"), pydantic.Field(alias="showInContentEditor")
    ] = None
    suppress_cms_path: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="suppressCmsPath"), pydantic.Field(alias="suppressCmsPath")
    ] = None
    tag_metadata: typing_extensions.Annotated[
        typing.Optional[typing.List[ContentModelsTagMetadataDefinition]],
        FieldMetadata(alias="tagMetadata"),
        pydantic.Field(alias="tagMetadata"),
    ] = None
    tag_metadata_items: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, ContentModelsTagMetadataItem]],
        FieldMetadata(alias="tagMetadataItems"),
        pydantic.Field(alias="tagMetadataItems"),
    ] = None
    type_of: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeOf"), pydantic.Field(alias="typeOf")
    ] = None
    usage_examples: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="usageExamples"), pydantic.Field(alias="usageExamples")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .content_models_content_type_property import ContentModelsContentTypeProperty

update_forward_refs(
    ContentModelsContentTypeDescription, ContentModelsContentTypeProperty=ContentModelsContentTypeProperty
)

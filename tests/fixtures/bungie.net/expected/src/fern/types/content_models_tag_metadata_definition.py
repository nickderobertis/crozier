

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .content_models_tag_metadata_item import ContentModelsTagMetadataItem


class ContentModelsTagMetadataDefinition(UniversalBaseModel):
    datatype: typing.Optional[str] = None
    description: typing.Optional[str] = None
    is_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")
    ] = None
    items: typing.Optional[typing.List[ContentModelsTagMetadataItem]] = None
    name: typing.Optional[str] = None
    order: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

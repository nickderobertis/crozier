

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .record_model_attachments import RecordModelAttachments
from .record_model_links_item import RecordModelLinksItem
from .record_model_properties import RecordModelProperties
from .record_model_source import RecordModelSource


class RecordModel(UniversalBaseModel):
    id: typing.Optional[str] = None
    ironclad_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ironcladId"), pydantic.Field(alias="ironcladId")
    ] = None
    type: typing.Optional[str] = None
    name: typing.Optional[str] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    properties: typing.Optional[RecordModelProperties] = None
    attachments: typing.Optional[RecordModelAttachments] = None
    links: typing.Optional[typing.List[RecordModelLinksItem]] = None
    parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    child_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="childIds"), pydantic.Field(alias="childIds")
    ] = None
    source: typing.Optional[RecordModelSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links
from .note_entity_name import NoteEntityName
from .note_reply import NoteReply


class Note(UniversalBaseModel):
    id: float
    company_id: typing_extensions.Annotated[float, FieldMetadata(alias="companyId"), pydantic.Field(alias="companyId")]
    entity_id: typing_extensions.Annotated[float, FieldMetadata(alias="entityId"), pydantic.Field(alias="entityId")]
    entity_name: typing_extensions.Annotated[
        NoteEntityName, FieldMetadata(alias="entityName"), pydantic.Field(alias="entityName")
    ]
    text: str
    created_by_id: typing_extensions.Annotated[
        float, FieldMetadata(alias="createdById"), pydantic.Field(alias="createdById")
    ]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    is_pinned: typing_extensions.Annotated[bool, FieldMetadata(alias="isPinned"), pydantic.Field(alias="isPinned")]
    parent_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    links: typing.List[Links]
    replies: typing.Optional[typing.List[NoteReply]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

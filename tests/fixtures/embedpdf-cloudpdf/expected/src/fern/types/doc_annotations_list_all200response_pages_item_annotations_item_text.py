

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_text_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_icon import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemText(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextReplyType],
        FieldMetadata(alias="replyType"),
        pydantic.Field(alias="replyType"),
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    actions: typing.Optional[PdfAnnotationActions] = None
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextColor
    opacity: float
    icon: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextIcon
    state: typing.Optional[str] = None
    state_model: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stateModel"), pydantic.Field(alias="stateModel")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

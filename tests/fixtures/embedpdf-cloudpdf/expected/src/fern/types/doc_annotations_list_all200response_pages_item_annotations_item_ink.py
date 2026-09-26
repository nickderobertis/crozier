

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_ink_list_item_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInkListItemItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_intent import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkIntent,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_ink_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInk(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    intent: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkIntent] = None
    ink_list: typing_extensions.Annotated[
        typing.List[typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkInkListItemItem]],
        FieldMetadata(alias="inkList"),
        pydantic.Field(alias="inkList"),
    ]
    rotation: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

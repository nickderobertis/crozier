

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_quad_points_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightQuadPointsItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_highlight_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlight(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemHighlightQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

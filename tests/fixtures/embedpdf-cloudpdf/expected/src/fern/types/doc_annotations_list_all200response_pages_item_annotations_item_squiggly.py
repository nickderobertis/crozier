

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_quad_points_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyQuadPointsItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquiggly(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyQuadPointsItem],
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

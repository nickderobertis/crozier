

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_squiggly_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyBlendMode,
)
from .doc_annotations_list200response_annotations_item_squiggly_color import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyColor,
)
from .doc_annotations_list200response_annotations_item_squiggly_flags import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyFlags,
)
from .doc_annotations_list200response_annotations_item_squiggly_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_squiggly_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo,
)
from .doc_annotations_list200response_annotations_item_squiggly_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyPage,
)
from .doc_annotations_list200response_annotations_item_squiggly_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_squiggly_rect import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyRect,
)
from .doc_annotations_list200response_annotations_item_squiggly_ref import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyRef,
)
from .doc_annotations_list200response_annotations_item_squiggly_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemSquiggly(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemSquigglyRef
    page: DocAnnotationsList200ResponseAnnotationsItemSquigglyPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquigglyIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemSquigglyFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemSquigglyRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquigglyBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquigglyReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemSquigglyColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItem],
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

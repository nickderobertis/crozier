

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_text_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemTextBlendMode,
)
from .doc_annotations_list200response_annotations_item_text_color import (
    DocAnnotationsList200ResponseAnnotationsItemTextColor,
)
from .doc_annotations_list200response_annotations_item_text_flags import (
    DocAnnotationsList200ResponseAnnotationsItemTextFlags,
)
from .doc_annotations_list200response_annotations_item_text_icon import (
    DocAnnotationsList200ResponseAnnotationsItemTextIcon,
)
from .doc_annotations_list200response_annotations_item_text_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemTextIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_text_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo,
)
from .doc_annotations_list200response_annotations_item_text_page import (
    DocAnnotationsList200ResponseAnnotationsItemTextPage,
)
from .doc_annotations_list200response_annotations_item_text_rect import (
    DocAnnotationsList200ResponseAnnotationsItemTextRect,
)
from .doc_annotations_list200response_annotations_item_text_ref import (
    DocAnnotationsList200ResponseAnnotationsItemTextRef,
)
from .doc_annotations_list200response_annotations_item_text_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemTextReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemText(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemTextRef
    page: DocAnnotationsList200ResponseAnnotationsItemTextPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemTextIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemTextFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemTextRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemTextBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemTextReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemTextColor
    opacity: float
    icon: DocAnnotationsList200ResponseAnnotationsItemTextIcon
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

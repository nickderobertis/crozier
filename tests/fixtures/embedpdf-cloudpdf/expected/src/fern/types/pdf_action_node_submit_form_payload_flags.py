

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdf_action_node_submit_form_payload_flags_format import PdfActionNodeSubmitFormPayloadFlagsFormat
from .pdf_action_node_submit_form_payload_flags_method import PdfActionNodeSubmitFormPayloadFlagsMethod


class PdfActionNodeSubmitFormPayloadFlags(UniversalBaseModel):
    raw: int
    exclude: bool
    include_no_value_fields: typing_extensions.Annotated[
        bool, FieldMetadata(alias="includeNoValueFields"), pydantic.Field(alias="includeNoValueFields")
    ]
    format: PdfActionNodeSubmitFormPayloadFlagsFormat
    method: PdfActionNodeSubmitFormPayloadFlagsMethod
    submit_coordinates: typing_extensions.Annotated[
        bool, FieldMetadata(alias="submitCoordinates"), pydantic.Field(alias="submitCoordinates")
    ]
    include_append_saves: typing_extensions.Annotated[
        bool, FieldMetadata(alias="includeAppendSaves"), pydantic.Field(alias="includeAppendSaves")
    ]
    include_annotations: typing_extensions.Annotated[
        bool, FieldMetadata(alias="includeAnnotations"), pydantic.Field(alias="includeAnnotations")
    ]
    canonical_format: typing_extensions.Annotated[
        bool, FieldMetadata(alias="canonicalFormat"), pydantic.Field(alias="canonicalFormat")
    ]
    excl_non_user_annots: typing_extensions.Annotated[
        bool, FieldMetadata(alias="exclNonUserAnnots"), pydantic.Field(alias="exclNonUserAnnots")
    ]
    excl_f_key: typing_extensions.Annotated[bool, FieldMetadata(alias="exclFKey"), pydantic.Field(alias="exclFKey")]
    embed_form: typing_extensions.Annotated[bool, FieldMetadata(alias="embedForm"), pydantic.Field(alias="embedForm")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

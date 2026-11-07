

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .callback_list_response_case_document_order_callbacks import CallbackListResponseCaseDocumentOrderCallbacks
from .callback_list_response_case_export_callbacks import CallbackListResponseCaseExportCallbacks


class CallbackListResponse(UniversalBaseModel):
    case_document_order_callbacks: typing_extensions.Annotated[
        CallbackListResponseCaseDocumentOrderCallbacks,
        FieldMetadata(alias="caseDocumentOrderCallbacks"),
        pydantic.Field(alias="caseDocumentOrderCallbacks"),
    ]
    case_export_callbacks: typing_extensions.Annotated[
        CallbackListResponseCaseExportCallbacks,
        FieldMetadata(alias="caseExportCallbacks"),
        pydantic.Field(alias="caseExportCallbacks"),
    ]
    object: str = pydantic.Field()
    """
    Name of the object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

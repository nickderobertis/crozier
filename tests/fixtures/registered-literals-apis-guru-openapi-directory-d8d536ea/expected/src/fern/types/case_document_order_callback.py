

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_document import CaseDocument
from .case_document_order_callback_status import CaseDocumentOrderCallbackStatus
from .exception import Exception
from .export_file import ExportFile


class CaseDocumentOrderCallback(UniversalBaseModel):
    callback_generated_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="callbackGeneratedDate"),
        pydantic.Field(alias="callbackGeneratedDate", description="Date when the job is run."),
    ] = None
    """
    Date when the job is run.
    """

    case_document: typing_extensions.Annotated[
        typing.Optional[CaseDocument], FieldMetadata(alias="caseDocument"), pydantic.Field(alias="caseDocument")
    ] = None
    case_document_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseDocumentId"),
        pydantic.Field(alias="caseDocumentId", description="UniCourt's Case Document ID."),
    ]
    """
    UniCourt's Case Document ID.
    """

    case_document_order_callback_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseDocumentOrderCallbackAPI"), pydantic.Field(alias="caseDocumentOrderCallbackAPI")
    ]
    case_document_order_callback_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseDocumentOrderCallbackId"),
        pydantic.Field(
            alias="caseDocumentOrderCallbackId", description="Unique Id for the Case Document Order Callback."
        ),
    ]
    """
    Unique Id for the Case Document Order Callback.
    """

    exception: typing.Optional[Exception] = None
    file: typing.Optional[ExportFile] = None
    object: str = pydantic.Field()
    """
    Name of the object.
    """

    status: CaseDocumentOrderCallbackStatus = pydantic.Field()
    """
    Status of the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

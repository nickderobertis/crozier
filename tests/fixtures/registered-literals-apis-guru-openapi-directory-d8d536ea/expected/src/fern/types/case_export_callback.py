

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_export_callback_status import CaseExportCallbackStatus
from .exception import Exception
from .export_file import ExportFile


class CaseExportCallback(UniversalBaseModel):
    callback_generated_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="callbackGeneratedDate"),
        pydantic.Field(alias="callbackGeneratedDate", description="Date when the job is run."),
    ] = None
    """
    Date when the job is run.
    """

    case_export_callback_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseExportCallbackAPI"), pydantic.Field(alias="caseExportCallbackAPI")
    ]
    case_export_callback_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseExportCallbackId"),
        pydantic.Field(alias="caseExportCallbackId", description="Unique Id for the Case Export Callback."),
    ]
    """
    Unique Id for the Case Export Callback.
    """

    case_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseId"),
        pydantic.Field(alias="caseId", description="Unique Id for a Case in UniCourt."),
    ]
    """
    Unique Id for a Case in UniCourt.
    """

    exception: typing.Optional[Exception] = None
    file: typing.Optional[ExportFile] = None
    object: str = pydantic.Field()
    """
    Name of the object.
    """

    status: CaseExportCallbackStatus = pydantic.Field()
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

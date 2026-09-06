

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .system_object import SystemObject


class CommunicationModelsFileUpload(UniversalBaseModel):
    created_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="CreatedDate"),
        pydantic.Field(alias="CreatedDate", description="The date the file was created"),
    ] = None
    """
    The date the file was created
    """

    dealer_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DealerID"),
        pydantic.Field(alias="DealerID", description="The Dearler ID"),
    ] = None
    """
    The Dearler ID
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description"),
    ] = None
    """
    The description
    """

    email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Email"),
        pydantic.Field(alias="Email", description="The email address provided with the file upload"),
    ] = None
    """
    The email address provided with the file upload
    """

    file_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="FileID"), pydantic.Field(alias="FileID", description="The file ID")
    ] = None
    """
    The file ID
    """

    file_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FileTypeID"),
        pydantic.Field(alias="FileTypeID", description="The File Type ID"),
    ] = None
    """
    The File Type ID
    """

    index_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="IndexData"),
        pydantic.Field(
            alias="IndexData",
            description="The Index Data for the File Upload. \r\n            Fields without a value are omitted.\r\n            Index Data may not be included in the response if no index data was requested.",
        ),
    ] = None
    """
    The Index Data for the File Upload. 
                Fields without a value are omitted.
                Index Data may not be included in the response if no index data was requested.
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name provided with the file upload"),
    ] = None
    """
    The name provided with the file upload
    """

    node_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="NodeID"), pydantic.Field(alias="NodeID", description="The node ID")
    ] = None
    """
    The node ID
    """

    phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Phone"),
        pydantic.Field(alias="Phone", description="The phone number provided with the file upload"),
    ] = None
    """
    The phone number provided with the file upload
    """

    stored_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, SystemObject]],
        FieldMetadata(alias="StoredData"),
        pydantic.Field(
            alias="StoredData",
            description="The Stored Data for the File Upload. \r\n            Fields without a value are omitted.\r\n            Stored Data may not be included in the response if no stored data was requested.",
        ),
    ] = None
    """
    The Stored Data for the File Upload. 
                Fields without a value are omitted.
                Stored Data may not be included in the response if no stored data was requested.
    """

    submission_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SubmissionCode"),
        pydantic.Field(alias="SubmissionCode", description="The submission code"),
    ] = None
    """
    The submission code
    """

    upload_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="UploadDate"),
        pydantic.Field(alias="UploadDate", description="The date the file was uploaded"),
    ] = None
    """
    The date the file was uploaded
    """

    version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Version"),
        pydantic.Field(alias="Version", description="The EDT version"),
    ] = None
    """
    The EDT version
    """

    voucher: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Voucher"),
        pydantic.Field(alias="Voucher", description="The voucher of the EDT instance"),
    ] = None
    """
    The voucher of the EDT instance
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

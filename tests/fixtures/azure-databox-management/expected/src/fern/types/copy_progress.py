

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .copy_progress_data_destination_type import CopyProgressDataDestinationType


class CopyProgress(UniversalBaseModel):
    """
    Copy progress.
    """

    account_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountId"),
        pydantic.Field(alias="accountId", description="Id of the account where the data needs to be uploaded."),
    ] = None
    """
    Id of the account where the data needs to be uploaded.
    """

    bytes_sent_to_cloud: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bytesSentToCloud"),
        pydantic.Field(alias="bytesSentToCloud", description="Amount of data uploaded by the job as of now."),
    ] = None
    """
    Amount of data uploaded by the job as of now.
    """

    data_destination_type: typing_extensions.Annotated[
        typing.Optional[CopyProgressDataDestinationType],
        FieldMetadata(alias="dataDestinationType"),
        pydantic.Field(alias="dataDestinationType", description="Data Destination Type."),
    ] = None
    """
    Data Destination Type.
    """

    files_errored_out: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="filesErroredOut"),
        pydantic.Field(alias="filesErroredOut", description="Number of files which could not be copied"),
    ] = None
    """
    Number of files which could not be copied
    """

    files_processed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="filesProcessed"),
        pydantic.Field(alias="filesProcessed", description="Number of files processed by the job as of now."),
    ] = None
    """
    Number of files processed by the job as of now.
    """

    invalid_file_bytes_uploaded: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="invalidFileBytesUploaded"),
        pydantic.Field(
            alias="invalidFileBytesUploaded",
            description="Total amount of data not adhering to azure naming conventions which were processed by automatic renaming",
        ),
    ] = None
    """
    Total amount of data not adhering to azure naming conventions which were processed by automatic renaming
    """

    invalid_files_processed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="invalidFilesProcessed"),
        pydantic.Field(
            alias="invalidFilesProcessed",
            description="Number of files not adhering to azure naming conventions which were processed by automatic renaming",
        ),
    ] = None
    """
    Number of files not adhering to azure naming conventions which were processed by automatic renaming
    """

    renamed_container_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="renamedContainerCount"),
        pydantic.Field(
            alias="renamedContainerCount",
            description="Number of folders not adhering to azure naming conventions which were processed by automatic renaming",
        ),
    ] = None
    """
    Number of folders not adhering to azure naming conventions which were processed by automatic renaming
    """

    storage_account_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="storageAccountName"),
        pydantic.Field(
            alias="storageAccountName", description="Name of the storage account where the data needs to be uploaded."
        ),
    ] = None
    """
    Name of the storage account where the data needs to be uploaded.
    """

    total_bytes_to_process: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalBytesToProcess"),
        pydantic.Field(alias="totalBytesToProcess", description="Total amount of data to be processed by the job."),
    ] = None
    """
    Total amount of data to be processed by the job.
    """

    total_files_to_process: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalFilesToProcess"),
        pydantic.Field(alias="totalFilesToProcess", description="Total number of files to be processed by the job."),
    ] = None
    """
    Total number of files to be processed by the job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

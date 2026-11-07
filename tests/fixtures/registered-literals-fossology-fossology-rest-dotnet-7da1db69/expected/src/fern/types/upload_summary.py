

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .upload_summary_clearing_status import UploadSummaryClearingStatus


class UploadSummary(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Upload id of the upload.
    """

    upload_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uploadName"),
        pydantic.Field(alias="uploadName", description="Display name of the upload."),
    ] = None
    """
    Display name of the upload.
    """

    assignee: typing.Optional[int] = pydantic.Field(default=None)
    """
    assignee id of the upload.
    """

    main_license: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mainLicense"),
        pydantic.Field(alias="mainLicense", description="Main license selected on the upload."),
    ] = None
    """
    Main license selected on the upload.
    """

    unique_licenses: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uniqueLicenses"),
        pydantic.Field(alias="uniqueLicenses", description="No. of unique licenses found."),
    ] = None
    """
    No. of unique licenses found.
    """

    total_licenses: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalLicenses"),
        pydantic.Field(alias="totalLicenses", description="Total no. of licenses found."),
    ] = None
    """
    Total no. of licenses found.
    """

    unique_concluded_licenses: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uniqueConcludedLicenses"),
        pydantic.Field(alias="uniqueConcludedLicenses", description="Unique licenses concluded."),
    ] = None
    """
    Unique licenses concluded.
    """

    total_concluded_licenses: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="totalConcludedLicenses"),
        pydantic.Field(alias="totalConcludedLicenses", description="Total concluded licenses."),
    ] = None
    """
    Total concluded licenses.
    """

    files_to_be_cleared: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="filesToBeCleared"),
        pydantic.Field(alias="filesToBeCleared", description="Files without clearing decisions."),
    ] = None
    """
    Files without clearing decisions.
    """

    files_cleared: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="filesCleared"),
        pydantic.Field(alias="filesCleared", description="Files with clearing decisions."),
    ] = None
    """
    Files with clearing decisions.
    """

    clearing_status: typing_extensions.Annotated[
        typing.Optional[UploadSummaryClearingStatus],
        FieldMetadata(alias="clearingStatus"),
        pydantic.Field(alias="clearingStatus", description="Upload is clearing status."),
    ] = None
    """
    Upload is clearing status.
    """

    copyright_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="copyrightCount"),
        pydantic.Field(alias="copyrightCount", description="No. of copyrights found in the upload."),
    ] = None
    """
    No. of copyrights found in the upload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

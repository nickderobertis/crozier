

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_list import ArtifactList
from .carrier import Carrier
from .creation_date import CreationDate
from .current_manifest import CurrentManifest
from .error_count import ErrorCount
from .job_id import JobId
from .job_type import JobType
from .location_code import LocationCode
from .location_message import LocationMessage
from .log_bucket import LogBucket
from .log_key import LogKey
from .progress_code import ProgressCode
from .progress_message import ProgressMessage
from .signature import Signature
from .tracking_number import TrackingNumber


class GetStatusOutput(UniversalBaseModel):
    """
    Output structure for the GetStatus operation.
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[JobId], FieldMetadata(alias="JobId"), pydantic.Field(alias="JobId")
    ] = None
    job_type: typing_extensions.Annotated[
        typing.Optional[JobType], FieldMetadata(alias="JobType"), pydantic.Field(alias="JobType")
    ] = None
    location_code: typing_extensions.Annotated[
        typing.Optional[LocationCode], FieldMetadata(alias="LocationCode"), pydantic.Field(alias="LocationCode")
    ] = None
    location_message: typing_extensions.Annotated[
        typing.Optional[LocationMessage],
        FieldMetadata(alias="LocationMessage"),
        pydantic.Field(alias="LocationMessage"),
    ] = None
    progress_code: typing_extensions.Annotated[
        typing.Optional[ProgressCode], FieldMetadata(alias="ProgressCode"), pydantic.Field(alias="ProgressCode")
    ] = None
    progress_message: typing_extensions.Annotated[
        typing.Optional[ProgressMessage],
        FieldMetadata(alias="ProgressMessage"),
        pydantic.Field(alias="ProgressMessage"),
    ] = None
    carrier: typing_extensions.Annotated[
        typing.Optional[Carrier], FieldMetadata(alias="Carrier"), pydantic.Field(alias="Carrier")
    ] = None
    tracking_number: typing_extensions.Annotated[
        typing.Optional[TrackingNumber], FieldMetadata(alias="TrackingNumber"), pydantic.Field(alias="TrackingNumber")
    ] = None
    log_bucket: typing_extensions.Annotated[
        typing.Optional[LogBucket], FieldMetadata(alias="LogBucket"), pydantic.Field(alias="LogBucket")
    ] = None
    log_key: typing_extensions.Annotated[
        typing.Optional[LogKey], FieldMetadata(alias="LogKey"), pydantic.Field(alias="LogKey")
    ] = None
    error_count: typing_extensions.Annotated[
        typing.Optional[ErrorCount], FieldMetadata(alias="ErrorCount"), pydantic.Field(alias="ErrorCount")
    ] = None
    signature: typing_extensions.Annotated[
        typing.Optional[Signature], FieldMetadata(alias="Signature"), pydantic.Field(alias="Signature")
    ] = None
    signature_file_contents: typing_extensions.Annotated[
        typing.Optional[Signature],
        FieldMetadata(alias="SignatureFileContents"),
        pydantic.Field(alias="SignatureFileContents"),
    ] = None
    current_manifest: typing_extensions.Annotated[
        typing.Optional[CurrentManifest],
        FieldMetadata(alias="CurrentManifest"),
        pydantic.Field(alias="CurrentManifest"),
    ] = None
    creation_date: typing_extensions.Annotated[
        typing.Optional[CreationDate], FieldMetadata(alias="CreationDate"), pydantic.Field(alias="CreationDate")
    ] = None
    artifact_list: typing_extensions.Annotated[
        typing.Optional[ArtifactList], FieldMetadata(alias="ArtifactList"), pydantic.Field(alias="ArtifactList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

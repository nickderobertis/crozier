

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_list import ArtifactList
from .job_id import JobId
from .job_type import JobType
from .signature import Signature
from .signature_file_contents import SignatureFileContents
from .warning_message import WarningMessage


class CreateJobOutput(UniversalBaseModel):
    """
    Output structure for the CreateJob operation.
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[JobId], FieldMetadata(alias="JobId"), pydantic.Field(alias="JobId")
    ] = None
    job_type: typing_extensions.Annotated[
        typing.Optional[JobType], FieldMetadata(alias="JobType"), pydantic.Field(alias="JobType")
    ] = None
    signature: typing_extensions.Annotated[
        typing.Optional[Signature], FieldMetadata(alias="Signature"), pydantic.Field(alias="Signature")
    ] = None
    signature_file_contents: typing_extensions.Annotated[
        typing.Optional[SignatureFileContents],
        FieldMetadata(alias="SignatureFileContents"),
        pydantic.Field(alias="SignatureFileContents"),
    ] = None
    warning_message: typing_extensions.Annotated[
        typing.Optional[WarningMessage], FieldMetadata(alias="WarningMessage"), pydantic.Field(alias="WarningMessage")
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

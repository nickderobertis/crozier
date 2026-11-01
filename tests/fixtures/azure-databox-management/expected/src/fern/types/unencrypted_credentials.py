

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_secrets import JobSecrets


class UnencryptedCredentials(UniversalBaseModel):
    """
    Unencrypted credentials for accessing device.
    """

    job_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="jobName"),
        pydantic.Field(alias="jobName", description="Name of the job."),
    ] = None
    """
    Name of the job.
    """

    job_secrets: typing_extensions.Annotated[
        typing.Optional[JobSecrets],
        FieldMetadata(alias="jobSecrets"),
        pydantic.Field(alias="jobSecrets", description="Secrets related to this job."),
    ] = None
    """
    Secrets related to this job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

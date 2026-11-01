

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .data_box_secret import DataBoxSecret
from .job_secrets import JobSecrets


class DataboxJobSecrets(JobSecrets):
    """
    The secrets related to a databox job.
    """

    pod_secrets: typing_extensions.Annotated[
        typing.Optional[typing.List[DataBoxSecret]],
        FieldMetadata(alias="podSecrets"),
        pydantic.Field(alias="podSecrets", description="Contains the list of secret objects for a job."),
    ] = None
    """
    Contains the list of secret objects for a job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

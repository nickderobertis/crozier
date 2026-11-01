

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .data_box_heavy_secret import DataBoxHeavySecret
from .job_secrets import JobSecrets


class DataBoxHeavyJobSecrets(JobSecrets):
    """
    The secrets related to a databox heavy job.
    """

    cabinet_pod_secrets: typing_extensions.Annotated[
        typing.Optional[typing.List[DataBoxHeavySecret]],
        FieldMetadata(alias="cabinetPodSecrets"),
        pydantic.Field(
            alias="cabinetPodSecrets", description="Contains the list of secret objects for a databox heavy job."
        ),
    ] = None
    """
    Contains the list of secret objects for a databox heavy job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

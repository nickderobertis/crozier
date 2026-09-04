

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .neutral_job_status import NeutralJobStatus


class JobRef(UniversalBaseModel):
    """
    Handle to the submitted job. `jobId` is opaque. An optional terminal `status` is the born-terminal fast-path for a synchronous backend.
    """

    job_id: typing_extensions.Annotated[str, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    status: typing.Optional[NeutralJobStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

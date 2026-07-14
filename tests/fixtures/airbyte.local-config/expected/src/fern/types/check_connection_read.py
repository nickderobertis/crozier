

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .check_connection_read_status import CheckConnectionReadStatus
from .synchronous_job_read import SynchronousJobRead


class CheckConnectionRead(UniversalBaseModel):
    job_info: typing_extensions.Annotated[SynchronousJobRead, FieldMetadata(alias="jobInfo")]
    message: typing.Optional[str] = None
    status: CheckConnectionReadStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

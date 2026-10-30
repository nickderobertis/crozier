

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_input_job_type import JobInputJobType
from .job_input_status import JobInputStatus


class JobInput(UniversalBaseModel):
    company: str
    position: str
    status: typing.Optional[JobInputStatus] = None
    job_type: typing_extensions.Annotated[
        typing.Optional[JobInputJobType], FieldMetadata(alias="jobType"), pydantic.Field(alias="jobType")
    ] = None
    job_location: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="jobLocation"), pydantic.Field(alias="jobLocation")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_type import JobType
from .resource_requirements import ResourceRequirements


class JobTypeResourceLimit(UniversalBaseModel):
    """
    sets resource requirements for a specific job type for an actor definition. these values override the default, if both are set.
    """

    job_type: typing_extensions.Annotated[JobType, FieldMetadata(alias="jobType")]
    resource_requirements: typing_extensions.Annotated[
        ResourceRequirements, FieldMetadata(alias="resourceRequirements")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

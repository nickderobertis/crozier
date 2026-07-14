

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_type_resource_limit import JobTypeResourceLimit
from .resource_requirements import ResourceRequirements


class ActorDefinitionResourceRequirements(UniversalBaseModel):
    """
    actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level.
    """

    default: typing.Optional[ResourceRequirements] = None
    job_specific: typing_extensions.Annotated[
        typing.Optional[typing.List[JobTypeResourceLimit]], FieldMetadata(alias="jobSpecific")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

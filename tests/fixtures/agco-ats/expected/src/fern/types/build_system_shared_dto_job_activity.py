

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_parameter_mapping import BuildSystemSharedDtoParameterMapping


class BuildSystemSharedDtoJobActivity(UniversalBaseModel):
    """
    A DTO for an IJobActivity
    """

    activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityID"),
        pydantic.Field(alias="ActivityID", description="The ID of the activity to be run as part of the job"),
    ] = None
    """
    The ID of the activity to be run as part of the job
    """

    job_activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobActivityID"),
        pydantic.Field(alias="JobActivityID", description="The ID of this job activity"),
    ] = None
    """
    The ID of this job activity
    """

    job_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="JobID"),
        pydantic.Field(alias="JobID", description="The ID of the job this job activity belongs to"),
    ] = None
    """
    The ID of the job this job activity belongs to
    """

    parameter_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoParameterMapping]],
        FieldMetadata(alias="ParameterMappings"),
        pydantic.Field(
            alias="ParameterMappings",
            description="The mapping of values from a source to be used for the activity parameters",
        ),
    ] = None
    """
    The mapping of values from a source to be used for the activity parameters
    """

    run_order: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="RunOrder"),
        pydantic.Field(alias="RunOrder", description="The order of this job activity relative to others in the job"),
    ] = None
    """
    The order of this job activity relative to others in the job
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_parameter_mapping import BuildSystemSharedDtoParameterMapping


class BuildSystemSharedDtoActivityStep(UniversalBaseModel):
    """
    A DTO for an IActivityStep
    """

    activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityID"),
        pydantic.Field(alias="ActivityID", description="The id of the activity this activity step belongs to"),
    ] = None
    """
    The id of the activity this activity step belongs to
    """

    activity_step_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityStepID"),
        pydantic.Field(alias="ActivityStepID", description="The id of this activity step"),
    ] = None
    """
    The id of this activity step
    """

    implementation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ImplementationID"),
        pydantic.Field(
            alias="ImplementationID",
            description="The implementation id which is used to look up the step implementation",
        ),
    ] = None
    """
    The implementation id which is used to look up the step implementation
    """

    parameter_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoParameterMapping]],
        FieldMetadata(alias="ParameterMappings"),
        pydantic.Field(
            alias="ParameterMappings",
            description="The mapping of values from a source to be used for the step parameters",
        ),
    ] = None
    """
    The mapping of values from a source to be used for the step parameters
    """

    run_order: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="RunOrder"),
        pydantic.Field(
            alias="RunOrder", description="The order of this activity step relative to other activity steps"
        ),
    ] = None
    """
    The order of this activity step relative to other activity steps
    """

    step_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="StepID"),
        pydantic.Field(alias="StepID", description="The id of the step"),
    ] = None
    """
    The id of the step
    """

    step_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StepName"),
        pydantic.Field(alias="StepName", description="The name of the step"),
    ] = None
    """
    The name of the step
    """

    use_config: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UseConfig"),
        pydantic.Field(
            alias="UseConfig",
            description="Indicates the configuration for the ActivityStep to use at runtime.  The build agent must provide this configuration",
        ),
    ] = None
    """
    Indicates the configuration for the ActivityStep to use at runtime.  The build agent must provide this configuration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

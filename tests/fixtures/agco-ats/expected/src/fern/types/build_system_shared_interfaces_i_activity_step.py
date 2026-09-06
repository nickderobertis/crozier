

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_interfaces_i_parameter_mapping import BuildSystemSharedInterfacesIParameterMapping


class BuildSystemSharedInterfacesIActivityStep(UniversalBaseModel):
    """
    IActivityStep
    """

    activity_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityID"),
        pydantic.Field(alias="ActivityID", description="ActivityID"),
    ] = None
    """
    ActivityID
    """

    activity_step_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ActivityStepID"),
        pydantic.Field(alias="ActivityStepID", description="ActivityStepID"),
    ] = None
    """
    ActivityStepID
    """

    implementation_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ImplementationID"),
        pydantic.Field(alias="ImplementationID", description="Implementation ID"),
    ] = None
    """
    Implementation ID
    """

    parameter_mappings: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedInterfacesIParameterMapping]],
        FieldMetadata(alias="ParameterMappings"),
        pydantic.Field(alias="ParameterMappings", description="ParameterMappings"),
    ] = None
    """
    ParameterMappings
    """

    run_order: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="RunOrder"), pydantic.Field(alias="RunOrder", description="run order")
    ] = None
    """
    run order
    """

    step_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="StepID"), pydantic.Field(alias="StepID", description="step id")
    ] = None
    """
    step id
    """

    step_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="StepName"), pydantic.Field(alias="StepName", description="steo name")
    ] = None
    """
    steo name
    """

    use_config: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UseConfig"),
        pydantic.Field(alias="UseConfig", description="UseConfig"),
    ] = None
    """
    UseConfig
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

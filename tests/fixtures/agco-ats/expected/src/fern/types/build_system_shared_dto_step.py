

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_dto_parameter import BuildSystemSharedDtoParameter


class BuildSystemSharedDtoStep(UniversalBaseModel):
    """
    Step
    """

    config_required: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="ConfigRequired"),
        pydantic.Field(
            alias="ConfigRequired",
            description="Indicates if the step requires configuration values to be provided by the build agent",
        ),
    ]
    """
    Indicates if the step requires configuration values to be provided by the build agent
    """

    deleted: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Deleted"),
        pydantic.Field(alias="Deleted", description="Read Only.  Indicates if the record is deleted."),
    ] = None
    """
    Read Only.  Indicates if the record is deleted.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="A description of the step to be presented to a user"),
    ] = None
    """
    A description of the step to be presented to a user
    """

    implementation_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ImplementationID"),
        pydantic.Field(
            alias="ImplementationID",
            description="The implementation ID used to lookup the step implementation when it is executed",
        ),
    ]
    """
    The implementation ID used to lookup the step implementation when it is executed
    """

    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The name of the step")
    ]
    """
    The name of the step
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[BuildSystemSharedDtoParameter]],
        FieldMetadata(alias="Parameters"),
        pydantic.Field(alias="Parameters", description="The parameters for this step"),
    ] = None
    """
    The parameters for this step
    """

    step_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="StepID"),
        pydantic.Field(alias="StepID", description="The ID of the step"),
    ] = None
    """
    The ID of the step
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

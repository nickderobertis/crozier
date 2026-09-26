

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .created_at_field import CreatedAtField
from .preconditioning_air_conditioning_failure_cause import PreconditioningAirConditioningFailureCause
from .preconditioning_air_conditioning_starting_cause import PreconditioningAirConditioningStartingCause
from .preconditioning_air_conditioning_status import PreconditioningAirConditioningStatus
from .preconditioning_program import PreconditioningProgram


class PreconditioningAirConditioning(CreatedAtField):
    status: typing.Optional[PreconditioningAirConditioningStatus] = pydantic.Field(default=None)
    """
    The status of the preconditioning feature.
    """

    starting_cause: typing_extensions.Annotated[
        typing.Optional[PreconditioningAirConditioningStartingCause],
        FieldMetadata(alias="startingCause"),
        pydantic.Field(alias="startingCause", description="starting cause"),
    ] = None
    """
    starting cause
    """

    failure_cause: typing_extensions.Annotated[
        typing.Optional[PreconditioningAirConditioningFailureCause],
        FieldMetadata(alias="failureCause"),
        pydantic.Field(alias="failureCause", description="failure cause"),
    ] = None
    """
    failure cause
    """

    programs: typing.Optional[typing.List[PreconditioningProgram]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

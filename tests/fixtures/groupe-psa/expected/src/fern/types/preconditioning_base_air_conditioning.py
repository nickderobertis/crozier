

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preconditioning_base_air_conditioning_failure_cause import PreconditioningBaseAirConditioningFailureCause
from .preconditioning_base_air_conditioning_starting_cause import PreconditioningBaseAirConditioningStartingCause
from .preconditioning_base_air_conditioning_status import PreconditioningBaseAirConditioningStatus
from .preconditioning_program import PreconditioningProgram


class PreconditioningBaseAirConditioning(UniversalBaseModel):
    status: typing.Optional[PreconditioningBaseAirConditioningStatus] = pydantic.Field(default=None)
    """
    The status of the preconditioning feature.
    """

    starting_cause: typing_extensions.Annotated[
        typing.Optional[PreconditioningBaseAirConditioningStartingCause],
        FieldMetadata(alias="startingCause"),
        pydantic.Field(alias="startingCause", description="starting cause"),
    ] = None
    """
    starting cause
    """

    failure_cause: typing_extensions.Annotated[
        typing.Optional[PreconditioningBaseAirConditioningFailureCause],
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

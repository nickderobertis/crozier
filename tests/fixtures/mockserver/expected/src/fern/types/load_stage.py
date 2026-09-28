

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .load_stage_type import LoadStageType
from .ramp_curve import RampCurve


class LoadStage(UniversalBaseModel):
    """
    one stage of a load profile, run in sequence: holds or ramps a setpoint for its duration
    """

    type: LoadStageType
    duration_millis: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="durationMillis"),
        pydantic.Field(
            alias="durationMillis",
            description="how long this stage runs in milliseconds (> 0); the sum across all stages is the total run length (max 3600000 = 1h)",
        ),
    ]
    """
    how long this stage runs in milliseconds (> 0); the sum across all stages is the total run length (max 3600000 = 1h)
    """

    curve: typing.Optional[RampCurve] = None
    vus: typing.Optional[int] = pydantic.Field(default=None)
    """
    VU hold: the number of virtual users to hold for the stage (max 50)
    """

    start_vus: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="startVus"),
        pydantic.Field(alias="startVus", description="VU ramp: virtual users at the start of the ramp"),
    ] = None
    """
    VU ramp: virtual users at the start of the ramp
    """

    end_vus: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="endVus"),
        pydantic.Field(alias="endVus", description="VU ramp: virtual users at the end of the ramp (max 50)"),
    ] = None
    """
    VU ramp: virtual users at the end of the ramp (max 50)
    """

    rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    RATE hold: arrival rate to hold, in iterations per second (max 5000)
    """

    start_rate: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="startRate"),
        pydantic.Field(
            alias="startRate", description="RATE ramp: arrival rate at the start of the ramp, in iterations per second"
        ),
    ] = None
    """
    RATE ramp: arrival rate at the start of the ramp, in iterations per second
    """

    end_rate: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="endRate"),
        pydantic.Field(
            alias="endRate",
            description="RATE ramp: arrival rate at the end of the ramp, in iterations per second (max 5000)",
        ),
    ] = None
    """
    RATE ramp: arrival rate at the end of the ramp, in iterations per second (max 5000)
    """

    max_vus: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxVus"),
        pydantic.Field(
            alias="maxVus",
            description="RATE stage only: optional cap on the auto-scaling virtual-user pool that runs the started iterations (defaults to the global virtual-user cap)",
        ),
    ] = None
    """
    RATE stage only: optional cap on the auto-scaling virtual-user pool that runs the started iterations (defaults to the global virtual-user cap)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QaCheckRequestMotionSweepCheckMonotonic(UniversalBaseModel):
    parameters: typing.Optional[typing.List[str]] = None
    samples: typing.Optional[float] = None
    max_delta_spike_ratio: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxDeltaSpikeRatio"), pydantic.Field(alias="maxDeltaSpikeRatio")
    ] = None
    check_monotonic: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="checkMonotonic"), pydantic.Field(alias="checkMonotonic")
    ] = None
    monotonic_parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="monotonicParameters"),
        pydantic.Field(alias="monotonicParameters"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

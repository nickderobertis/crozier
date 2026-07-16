

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .detect_stack_resource_drift_output_stack_resource_drift import DetectStackResourceDriftOutputStackResourceDrift


class DetectStackResourceDriftOutput(UniversalBaseModel):
    stack_resource_drift: typing_extensions.Annotated[
        DetectStackResourceDriftOutputStackResourceDrift, FieldMetadata(alias="StackResourceDrift")
    ] = pydantic.Field()
    """
    Information about whether the resource's actual configuration has drifted from its expected template configuration, including actual and expected property values and any differences detected.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

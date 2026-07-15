

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LatencyDescriptor(UniversalBaseModel):
    max_latency: typing_extensions.Annotated[int, FieldMetadata(alias="maxLatency")] = pydantic.Field()
    """
    The value of the maximum latency in nano seconds tolerated by the MEC application. See note.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

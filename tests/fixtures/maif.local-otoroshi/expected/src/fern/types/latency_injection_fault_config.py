

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LatencyInjectionFaultConfig(UniversalBaseModel):
    """
    Config for large latency injection fault
    """

    from_: typing_extensions.Annotated[int, FieldMetadata(alias="from")] = pydantic.Field()
    """
    The start range of latency added to the request
    """

    ratio: float = pydantic.Field()
    """
    The percentage of requests affected by this fault. Value should be between 0.0 and 1.0
    """

    to: int = pydantic.Field()
    """
    The end range of latency added to the request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

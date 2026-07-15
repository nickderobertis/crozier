

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResourceRequirements(UniversalBaseModel):
    """
    optional resource requirements to run workers (blank for unbounded allocations)
    """

    cpu_limit: typing.Optional[str] = None
    cpu_request: typing.Optional[str] = None
    memory_limit: typing.Optional[str] = None
    memory_request: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

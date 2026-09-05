

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HealthResponse(UniversalBaseModel):
    ready: bool
    mode: str = pydantic.Field()
    """
    Configured database mode.
    """

    index_runtime: str = pydantic.Field()
    """
    Stable index-runtime readiness code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

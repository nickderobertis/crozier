

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RerankResultUsage(UniversalBaseModel):
    """
    Usage statistics for the model inference.
    """

    rerank_units: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of rerank units consumed by this operation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

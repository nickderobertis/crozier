

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OtelBatchSpanProcessorConfig(UniversalBaseModel):
    max_export_batch_size: typing.Optional[float] = pydantic.Field(default=None)
    """
    The maximum batch size of every export. It must be smaller or equal to maxQueueSize (not yet configurable). Default 512.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigSflow(UniversalBaseModel):
    collector: typing.Optional[str] = None
    collectorport: typing.Optional[int] = None
    encoding_type: typing.Optional[str] = None
    filename: typing.Optional[str] = None
    flows_per_min: typing.Optional[int] = None
    include_samples: typing.Optional[str] = None
    records_per_sample: typing.Optional[str] = None
    samples_per_datagram: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

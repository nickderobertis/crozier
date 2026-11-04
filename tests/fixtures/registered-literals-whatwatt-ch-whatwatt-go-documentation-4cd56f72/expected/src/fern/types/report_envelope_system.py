

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReportEnvelopeSystem(UniversalBaseModel):
    id: typing.Optional[str] = None
    date_time: typing.Optional[str] = None
    date_time_local: typing.Optional[str] = None
    date_time_utc: typing.Optional[str] = None
    boot_id: typing.Optional[str] = None
    time_since_boot: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

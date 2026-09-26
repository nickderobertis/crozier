

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cn_statistics_hlen import CnStatisticsHlen
from .cn_statistics_keys import CnStatisticsKeys
from .cn_statistics_klen import CnStatisticsKlen
from .cn_statistics_ptombs import CnStatisticsPtombs
from .cn_statistics_tombs import CnStatisticsTombs
from .cn_statistics_vgarb import CnStatisticsVgarb
from .cn_statistics_vlen import CnStatisticsVlen


class CnStatistics(UniversalBaseModel):
    dgen: typing.Optional[int] = None
    keys: typing.Optional[CnStatisticsKeys] = None
    tombs: typing.Optional[CnStatisticsTombs] = None
    ptombs: typing.Optional[CnStatisticsPtombs] = None
    hlen: typing.Optional[CnStatisticsHlen] = None
    klen: typing.Optional[CnStatisticsKlen] = None
    vlen: typing.Optional[CnStatisticsVlen] = None
    vgarb: typing.Optional[CnStatisticsVgarb] = None
    hblocks: typing.Optional[int] = None
    kblocks: typing.Optional[int] = None
    vblocks: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

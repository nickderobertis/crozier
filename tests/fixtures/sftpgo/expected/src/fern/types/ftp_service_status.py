

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ftp_passive_port_range import FtpPassivePortRange
from .ftpd_binding import FtpdBinding


class FtpServiceStatus(UniversalBaseModel):
    is_active: typing.Optional[bool] = None
    bindings: typing.Optional[typing.List[FtpdBinding]] = None
    passive_port_range: typing.Optional[FtpPassivePortRange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

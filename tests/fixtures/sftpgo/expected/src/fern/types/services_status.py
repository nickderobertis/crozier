

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_provider_status import DataProviderStatus
from .ftp_service_status import FtpServiceStatus
from .mfa_status import MfaStatus
from .services_status_allow_list import ServicesStatusAllowList
from .services_status_defender import ServicesStatusDefender
from .services_status_rate_limiters import ServicesStatusRateLimiters
from .ssh_service_status import SshServiceStatus
from .web_dav_service_status import WebDavServiceStatus


class ServicesStatus(UniversalBaseModel):
    ssh: typing.Optional[SshServiceStatus] = None
    ftp: typing.Optional[FtpServiceStatus] = None
    webdav: typing.Optional[WebDavServiceStatus] = None
    data_provider: typing.Optional[DataProviderStatus] = None
    defender: typing.Optional[ServicesStatusDefender] = None
    mfa: typing.Optional[MfaStatus] = None
    allow_list: typing.Optional[ServicesStatusAllowList] = None
    rate_limiters: typing.Optional[ServicesStatusRateLimiters] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

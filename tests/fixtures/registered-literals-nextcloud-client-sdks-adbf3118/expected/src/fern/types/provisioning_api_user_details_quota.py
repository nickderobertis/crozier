

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_user_details_quota_quota import ProvisioningApiUserDetailsQuotaQuota


class ProvisioningApiUserDetailsQuota(UniversalBaseModel):
    free: typing.Optional[int] = None
    quota: ProvisioningApiUserDetailsQuotaQuota
    relative: typing.Optional[float] = None
    total: typing.Optional[int] = None
    used: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

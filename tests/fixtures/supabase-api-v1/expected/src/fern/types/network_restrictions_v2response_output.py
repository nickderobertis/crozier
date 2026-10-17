

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .network_restrictions_v2response_output_config import NetworkRestrictionsV2ResponseOutputConfig
from .network_restrictions_v2response_output_entitlement import NetworkRestrictionsV2ResponseOutputEntitlement
from .network_restrictions_v2response_output_old_config import NetworkRestrictionsV2ResponseOutputOldConfig
from .network_restrictions_v2response_output_status import NetworkRestrictionsV2ResponseOutputStatus


class NetworkRestrictionsV2ResponseOutput(UniversalBaseModel):
    entitlement: NetworkRestrictionsV2ResponseOutputEntitlement
    config: NetworkRestrictionsV2ResponseOutputConfig = pydantic.Field()
    """
    At any given point in time, this is the config that the user has requested be applied to their project. The `status` field indicates if it has been applied to the project, or is pending. When an updated config is received, the applied config is moved to `old_config`.
    """

    old_config: typing.Optional[NetworkRestrictionsV2ResponseOutputOldConfig] = pydantic.Field(default=None)
    """
    Populated when a new config has been received, but not registered as successfully applied to a project.
    """

    updated_at: typing.Optional[dt.datetime] = None
    applied_at: typing.Optional[dt.datetime] = None
    status: NetworkRestrictionsV2ResponseOutputStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

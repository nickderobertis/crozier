

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .network_restrictions_response_output_config import NetworkRestrictionsResponseOutputConfig
from .network_restrictions_response_output_entitlement import NetworkRestrictionsResponseOutputEntitlement
from .network_restrictions_response_output_old_config import NetworkRestrictionsResponseOutputOldConfig
from .network_restrictions_response_output_status import NetworkRestrictionsResponseOutputStatus


class NetworkRestrictionsResponseOutput(UniversalBaseModel):
    entitlement: NetworkRestrictionsResponseOutputEntitlement
    config: NetworkRestrictionsResponseOutputConfig = pydantic.Field()
    """
    At any given point in time, this is the config that the user has requested be applied to their project. The `status` field indicates if it has been applied to the project, or is pending. When an updated config is received, the applied config is moved to `old_config`.
    """

    old_config: typing.Optional[NetworkRestrictionsResponseOutputOldConfig] = pydantic.Field(default=None)
    """
    Populated when a new config has been received, but not registered as successfully applied to a project.
    """

    status: NetworkRestrictionsResponseOutputStatus
    updated_at: typing.Optional[dt.datetime] = None
    applied_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

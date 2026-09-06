

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entitlement_tenant_fulfillment_status_response import EntitlementTenantFulfillmentStatusResponse
from .entitlement_types import EntitlementTypes
from .snowflake_type import SnowflakeType


class EntitlementResponse(UniversalBaseModel):
    id: SnowflakeType
    sku_id: SnowflakeType
    application_id: SnowflakeType
    user_id: SnowflakeType
    guild_id: typing.Optional[SnowflakeType] = None
    deleted: bool
    starts_at: typing.Optional[dt.datetime] = None
    ends_at: typing.Optional[dt.datetime] = None
    type: EntitlementTypes
    fulfilled_at: typing.Optional[dt.datetime] = None
    fulfillment_status: typing.Optional[EntitlementTenantFulfillmentStatusResponse] = None
    consumed: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

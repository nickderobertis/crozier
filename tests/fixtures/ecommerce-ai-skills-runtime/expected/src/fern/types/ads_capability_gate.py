

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ads_capability_gate_checks_item import AdsCapabilityGateChecksItem
from .ads_capability_gate_observed_capabilities_item import AdsCapabilityGateObservedCapabilitiesItem
from .ads_capability_gate_region import AdsCapabilityGateRegion
from .ads_capability_gate_required_capabilities_item import AdsCapabilityGateRequiredCapabilitiesItem
from .ads_capability_gate_status import AdsCapabilityGateStatus


class AdsCapabilityGate(UniversalBaseModel):
    id: str
    tenant_id: str
    connector_account_id: str
    created_by: str
    status: AdsCapabilityGateStatus
    region: AdsCapabilityGateRegion
    profile_id: str
    required_capabilities: typing.List[AdsCapabilityGateRequiredCapabilitiesItem]
    observed_capabilities: typing.List[AdsCapabilityGateObservedCapabilitiesItem]
    checks: typing.List[AdsCapabilityGateChecksItem]
    request_ids: typing.List[str]
    retry_after_seconds: typing.Optional[int] = None
    attestation_reference: typing.Optional[str] = None
    error_code: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    checked_at: typing.Optional[dt.datetime] = None
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

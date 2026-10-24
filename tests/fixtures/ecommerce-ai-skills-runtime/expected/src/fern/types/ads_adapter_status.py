

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ads_adapter_status_reason_codes_item import AdsAdapterStatusReasonCodesItem
from .ads_adapter_status_region import AdsAdapterStatusRegion
from .ads_adapter_status_status import AdsAdapterStatusStatus


class AdsAdapterStatus(UniversalBaseModel):
    status: AdsAdapterStatusStatus
    adapter_registered: bool
    write_operations: typing.List[str]
    reason_codes: typing.List[AdsAdapterStatusReasonCodesItem]
    connector_account_id: typing.Optional[str] = None
    gate_id: typing.Optional[str] = None
    gate_checked_at: typing.Optional[dt.datetime] = None
    account_updated_at: typing.Optional[dt.datetime] = None
    profile_id: typing.Optional[str] = None
    region: typing.Optional[AdsAdapterStatusRegion] = None
    evaluated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .proposal_risk import ProposalRisk
from .shopify_sync_products_proposal_payload import ShopifySyncProductsProposalPayload


class ShopifySyncProductsProposalCreateRequest(UniversalBaseModel):
    daily_ops_run_id: str
    priority_rank: int
    rollback_plan: str
    payload: ShopifySyncProductsProposalPayload
    risk: ProposalRisk
    expires_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_ads_campaign_update_proposal_payload import AmazonAdsCampaignUpdateProposalPayload
from .amazon_spapi_import_report_proposal_payload import AmazonSpapiImportReportProposalPayload
from .human_review_proposal_payload import HumanReviewProposalPayload
from .proposal_risk import ProposalRisk
from .shopify_sync_products_proposal_payload import ShopifySyncProductsProposalPayload


class ProposalCreateRequest_HumanReview(UniversalBaseModel):
    operation: typing.Literal["human.review"] = "human.review"
    daily_ops_run_id: str
    priority_rank: int
    rollback_plan: str
    payload: HumanReviewProposalPayload
    risk: ProposalRisk
    expires_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProposalCreateRequest_ShopifySyncProducts(UniversalBaseModel):
    operation: typing.Literal["shopify.sync_products"] = "shopify.sync_products"
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


class ProposalCreateRequest_AmazonSpapiImportReport(UniversalBaseModel):
    operation: typing.Literal["amazon_spapi.import_report"] = "amazon_spapi.import_report"
    daily_ops_run_id: str
    priority_rank: int
    rollback_plan: str
    payload: AmazonSpapiImportReportProposalPayload
    risk: ProposalRisk
    expires_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProposalCreateRequest_AmazonAdsCampaignUpdate(UniversalBaseModel):
    operation: typing.Literal["amazon_ads.campaign_update"] = "amazon_ads.campaign_update"
    daily_ops_run_id: str
    priority_rank: int
    rollback_plan: str
    payload: AmazonAdsCampaignUpdateProposalPayload
    risk: ProposalRisk
    expires_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProposalCreateRequest = typing_extensions.Annotated[
    typing.Union[
        ProposalCreateRequest_HumanReview,
        ProposalCreateRequest_ShopifySyncProducts,
        ProposalCreateRequest_AmazonSpapiImportReport,
        ProposalCreateRequest_AmazonAdsCampaignUpdate,
    ],
    pydantic.Field(discriminator="operation"),
]

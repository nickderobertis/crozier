

import typing

from .amazon_ads_campaign_update_proposal_payload import AmazonAdsCampaignUpdateProposalPayload
from .amazon_spapi_import_report_proposal_payload import AmazonSpapiImportReportProposalPayload
from .human_review_proposal_payload import HumanReviewProposalPayload
from .shopify_sync_products_proposal_payload import ShopifySyncProductsProposalPayload

ProposalPayload = typing.Union[
    HumanReviewProposalPayload,
    ShopifySyncProductsProposalPayload,
    AmazonSpapiImportReportProposalPayload,
    AmazonAdsCampaignUpdateProposalPayload,
]

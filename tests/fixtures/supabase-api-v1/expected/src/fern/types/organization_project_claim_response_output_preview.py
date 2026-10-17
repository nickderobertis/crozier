

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .organization_project_claim_response_output_preview_errors_item import (
    OrganizationProjectClaimResponseOutputPreviewErrorsItem,
)
from .organization_project_claim_response_output_preview_info_item import (
    OrganizationProjectClaimResponseOutputPreviewInfoItem,
)
from .organization_project_claim_response_output_preview_members_exceeding_free_project_limit_item import (
    OrganizationProjectClaimResponseOutputPreviewMembersExceedingFreeProjectLimitItem,
)
from .organization_project_claim_response_output_preview_source_subscription_plan import (
    OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan,
)
from .organization_project_claim_response_output_preview_target_subscription_plan import (
    OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan,
)
from .organization_project_claim_response_output_preview_warnings_item import (
    OrganizationProjectClaimResponseOutputPreviewWarningsItem,
)


class OrganizationProjectClaimResponseOutputPreview(UniversalBaseModel):
    valid: bool
    warnings: typing.List[OrganizationProjectClaimResponseOutputPreviewWarningsItem]
    errors: typing.List[OrganizationProjectClaimResponseOutputPreviewErrorsItem]
    info: typing.List[OrganizationProjectClaimResponseOutputPreviewInfoItem]
    members_exceeding_free_project_limit: typing.List[
        OrganizationProjectClaimResponseOutputPreviewMembersExceedingFreeProjectLimitItem
    ]
    source_subscription_plan: OrganizationProjectClaimResponseOutputPreviewSourceSubscriptionPlan
    target_subscription_plan: typing.Optional[OrganizationProjectClaimResponseOutputPreviewTargetSubscriptionPlan] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

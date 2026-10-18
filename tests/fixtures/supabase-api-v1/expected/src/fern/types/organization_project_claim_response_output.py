

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .organization_project_claim_response_output_preview import OrganizationProjectClaimResponseOutputPreview
from .organization_project_claim_response_output_project import OrganizationProjectClaimResponseOutputProject


class OrganizationProjectClaimResponseOutput(UniversalBaseModel):
    project: OrganizationProjectClaimResponseOutputProject
    preview: OrganizationProjectClaimResponseOutputPreview
    expires_at: str
    created_at: str
    created_by: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1organization_slug_response_output_allowed_release_channels_item import (
    V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem,
)
from .v1organization_slug_response_output_opt_in_tags_item import V1OrganizationSlugResponseOutputOptInTagsItem
from .v1organization_slug_response_output_plan import V1OrganizationSlugResponseOutputPlan


class V1OrganizationSlugResponseOutput(UniversalBaseModel):
    id: str
    name: str
    plan: typing.Optional[V1OrganizationSlugResponseOutputPlan] = None
    opt_in_tags: typing.List[V1OrganizationSlugResponseOutputOptInTagsItem]
    allowed_release_channels: typing.List[V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_provider_resource_associations_register_response_not_applicable_reason import (
    PostInternalProviderResourceAssociationsRegisterResponseNotApplicableReason,
)


class PostInternalProviderResourceAssociationsRegisterResponseNotApplicable(UniversalBaseModel):
    reason: PostInternalProviderResourceAssociationsRegisterResponseNotApplicableReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

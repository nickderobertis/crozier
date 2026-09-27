

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .requires_reconsent_info_policies_item import RequiresReconsentInfoPoliciesItem


class RequiresReconsentInfo(UniversalBaseModel):
    policies: typing.List[RequiresReconsentInfoPoliciesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

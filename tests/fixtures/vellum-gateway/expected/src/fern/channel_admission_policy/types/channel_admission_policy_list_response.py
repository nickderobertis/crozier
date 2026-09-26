

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_admission_policy_list_response_policies_item import ChannelAdmissionPolicyListResponsePoliciesItem


class ChannelAdmissionPolicyListResponse(UniversalBaseModel):
    policies: typing.List[ChannelAdmissionPolicyListResponsePoliciesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

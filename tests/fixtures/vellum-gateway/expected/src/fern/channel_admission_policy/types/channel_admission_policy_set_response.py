

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_admission_policy_set_response_policy import ChannelAdmissionPolicySetResponsePolicy


class ChannelAdmissionPolicySetResponse(UniversalBaseModel):
    policy: ChannelAdmissionPolicySetResponsePolicy

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

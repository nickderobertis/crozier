

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_connection_policy_target_response_meta import ListConnectionPolicyTargetResponseMeta
from .voice_v1connection_policy_connection_policy_target import VoiceV1ConnectionPolicyConnectionPolicyTarget


class ListConnectionPolicyTargetResponse(UniversalBaseModel):
    meta: typing.Optional[ListConnectionPolicyTargetResponseMeta] = None
    targets: typing.Optional[typing.List[VoiceV1ConnectionPolicyConnectionPolicyTarget]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_connection_policy_response_meta import ListConnectionPolicyResponseMeta
from .voice_v1connection_policy import VoiceV1ConnectionPolicy


class ListConnectionPolicyResponse(UniversalBaseModel):
    connection_policies: typing.Optional[typing.List[VoiceV1ConnectionPolicy]] = None
    meta: typing.Optional[ListConnectionPolicyResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

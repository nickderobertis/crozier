

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_byoc_trunk_response_meta import ListByocTrunkResponseMeta
from .voice_v1byoc_trunk import VoiceV1ByocTrunk


class ListByocTrunkResponse(UniversalBaseModel):
    byoc_trunks: typing.Optional[typing.List[VoiceV1ByocTrunk]] = None
    meta: typing.Optional[ListByocTrunkResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

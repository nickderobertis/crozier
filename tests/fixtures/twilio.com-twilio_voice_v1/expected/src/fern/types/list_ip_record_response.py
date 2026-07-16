

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_ip_record_response_meta import ListIpRecordResponseMeta
from .voice_v1ip_record import VoiceV1IpRecord


class ListIpRecordResponse(UniversalBaseModel):
    ip_records: typing.Optional[typing.List[VoiceV1IpRecord]] = None
    meta: typing.Optional[ListIpRecordResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_source_ip_mapping_response_meta import ListSourceIpMappingResponseMeta
from .voice_v1source_ip_mapping import VoiceV1SourceIpMapping


class ListSourceIpMappingResponse(UniversalBaseModel):
    meta: typing.Optional[ListSourceIpMappingResponseMeta] = None
    source_ip_mappings: typing.Optional[typing.List[VoiceV1SourceIpMapping]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

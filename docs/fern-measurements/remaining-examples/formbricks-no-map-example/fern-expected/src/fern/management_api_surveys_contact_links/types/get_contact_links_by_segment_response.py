

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_contact_links_by_segment_response_data_item import GetContactLinksBySegmentResponseDataItem
from .get_contact_links_by_segment_response_meta import GetContactLinksBySegmentResponseMeta


class GetContactLinksBySegmentResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetContactLinksBySegmentResponseDataItem]] = None
    meta: typing.Optional[GetContactLinksBySegmentResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

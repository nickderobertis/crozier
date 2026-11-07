

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_tracking_snippet_response_data import GetTrackingSnippetResponseData
from .get_tracking_snippet_response_meta import GetTrackingSnippetResponseMeta


class GetTrackingSnippetResponse(UniversalBaseModel):
    meta: GetTrackingSnippetResponseMeta
    data: GetTrackingSnippetResponseData = pydantic.Field()
    """
    A snippet
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

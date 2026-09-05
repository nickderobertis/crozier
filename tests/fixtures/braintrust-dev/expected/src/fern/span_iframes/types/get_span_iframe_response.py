

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.span_i_frame import SpanIFrame


class GetSpanIframeResponse(UniversalBaseModel):
    objects: typing.List[SpanIFrame] = pydantic.Field()
    """
    A list of span_iframe objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

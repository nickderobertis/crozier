

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .landing_event_request_cta import LandingEventRequestCta


class LandingEventRequest(UniversalBaseModel):
    cta: LandingEventRequestCta
    path: str = pydantic.Field()
    """
    Local pathname starting with a single slash, without query or fragment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

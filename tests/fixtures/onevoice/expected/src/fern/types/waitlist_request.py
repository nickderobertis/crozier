

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .waitlist_request_pain import WaitlistRequestPain
from .waitlist_request_plan import WaitlistRequestPlan
from .waitlist_request_source import WaitlistRequestSource
from .waitlist_request_sphere import WaitlistRequestSphere


class WaitlistRequest(UniversalBaseModel):
    """
    Public closed-beta waitlist signup submitted from the marketing
    landing. Only email and the processing-consent flag are required; the
    segmentation fields are optional. Enums are inlined (not $ref) so the
    generated struct carries validate:oneof tags.
    """

    email: str
    sphere: typing.Optional[WaitlistRequestSphere] = pydantic.Field(default=None)
    """
    Optional organization-sphere segment.
    """

    pain: typing.Optional[WaitlistRequestPain] = pydantic.Field(default=None)
    """
    Optional strongest-pain segment.
    """

    source: typing.Optional[WaitlistRequestSource] = pydantic.Field(default=None)
    """
    Optional latest signup source; omitted values preserve existing attribution.
    """

    plan: typing.Optional[WaitlistRequestPlan] = pydantic.Field(default=None)
    """
    Optional requested plan; omitted values preserve existing interest.
    """

    consent: bool = pydantic.Field()
    """
    Must be true — the visitor ticked the personal-data-processing
    consent checkbox. A false or absent value fails validation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

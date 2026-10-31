

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConsentRequest(UniversalBaseModel):
    citizen_identity: str = pydantic.Field()
    """
    Opaque citizen identifier bound by PASS/공동인증서 at collection time.
    """

    scopes: typing.List[str] = pydantic.Field()
    """
    Scope entries shaped as `<tool_id>:<verb>[:resource]`.
    """

    dpa_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Non-null when any scope is PII-bound (FR-014).
    """

    synthesis_consent: bool = pydantic.Field()
    """
    Separate consent for the LLM-synthesis controller-level carve-out (FR-015).
    """

    expires_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

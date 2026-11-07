

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .check_advisories_response_active_advisories_item import CheckAdvisoriesResponseActiveAdvisoriesItem


class CheckAdvisoriesResponse(UniversalBaseModel):
    deprecated: typing.Optional[typing.List[str]] = None
    warned: typing.Optional[typing.List[str]] = None
    revoked: typing.Optional[typing.List[str]] = None
    active_advisories: typing.Optional[typing.List[CheckAdvisoriesResponseActiveAdvisoriesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_business_card_website import UserBusinessCardWebsite


class UserBusinessCard(UniversalBaseModel):
    company_name: typing.Optional[str] = None
    company_size: typing.Optional[str] = None
    headline: typing.Optional[str] = None
    industry: typing.Optional[str] = None
    interest_tags: typing.Optional[typing.List[str]] = None
    job_position: typing.Optional[str] = None
    summary: typing.Optional[str] = None
    website: typing.Optional[UserBusinessCardWebsite] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

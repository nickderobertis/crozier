

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetUserEmailsResponse(UniversalBaseModel):
    associated_accounts: typing.List[typing.Any]
    email: str
    secondary_emails: typing.List[typing.Any]
    unconfirmed_emails: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

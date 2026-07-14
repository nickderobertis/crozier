

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetUserResponseUserUserAuthTokensItem(UniversalBaseModel):
    browser: str
    client_ip: str
    created_at: str
    device: str
    icon: str
    id: int
    is_active: bool
    location: str
    os: str
    seen_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

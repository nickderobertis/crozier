

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateInviteResponse(UniversalBaseModel):
    created_at: typing.Optional[str] = None
    custom_message: typing.Optional[str] = None
    email: typing.Optional[str] = None
    emailed: typing.Optional[bool] = None
    expired: typing.Optional[bool] = None
    expires_at: typing.Optional[str] = None
    groups: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    id: typing.Optional[int] = None
    link: typing.Optional[str] = None
    topics: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    updated_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

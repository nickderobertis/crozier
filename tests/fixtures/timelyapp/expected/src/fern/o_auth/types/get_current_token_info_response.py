

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_current_token_info_response_application import GetCurrentTokenInfoResponseApplication


class GetCurrentTokenInfoResponse(UniversalBaseModel):
    resource_owner_id: typing.Optional[int] = None
    scope: typing.Optional[typing.List[str]] = None
    expires_in: typing.Optional[int] = None
    application: typing.Optional[GetCurrentTokenInfoResponseApplication] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

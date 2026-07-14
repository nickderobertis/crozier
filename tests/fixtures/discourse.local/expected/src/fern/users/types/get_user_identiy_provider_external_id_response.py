

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_identiy_provider_external_id_response_user import GetUserIdentiyProviderExternalIdResponseUser


class GetUserIdentiyProviderExternalIdResponse(UniversalBaseModel):
    user: GetUserIdentiyProviderExternalIdResponseUser
    user_badges: typing.List[typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

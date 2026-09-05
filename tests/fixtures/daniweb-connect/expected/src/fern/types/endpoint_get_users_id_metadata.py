

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_pagination import ApiPagination
from .user_data import UserData


class EndpointGetUsersIdMetadata(UniversalBaseModel):
    data: typing.Optional[typing.List[UserData]] = None
    pagination: typing.Optional[ApiPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

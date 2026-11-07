

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_user_to_account_response_meta import AddUserToAccountResponseMeta


class AddUserToAccountResponse(UniversalBaseModel):
    meta: AddUserToAccountResponseMeta
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

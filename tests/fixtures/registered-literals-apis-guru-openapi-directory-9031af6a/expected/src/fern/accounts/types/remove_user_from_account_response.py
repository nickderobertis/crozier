

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remove_user_from_account_response_meta import RemoveUserFromAccountResponseMeta


class RemoveUserFromAccountResponse(UniversalBaseModel):
    meta: RemoveUserFromAccountResponseMeta
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

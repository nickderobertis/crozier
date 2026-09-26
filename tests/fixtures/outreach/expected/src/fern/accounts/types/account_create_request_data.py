

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_create_request_data_attributes import AccountCreateRequestDataAttributes


class AccountCreateRequestData(UniversalBaseModel):
    type: str
    attributes: AccountCreateRequestDataAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_update_request_data_attributes import AccountUpdateRequestDataAttributes


class AccountUpdateRequestData(UniversalBaseModel):
    type: str
    id: int
    attributes: typing.Optional[AccountUpdateRequestDataAttributes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

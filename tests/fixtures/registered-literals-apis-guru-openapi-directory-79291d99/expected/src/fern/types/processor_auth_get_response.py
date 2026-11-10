

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_base import AccountBase
from .processor_number import ProcessorNumber
from .request_id import RequestId


class ProcessorAuthGetResponse(UniversalBaseModel):
    """
    ProcessorAuthGetResponse defines the response schema for `/processor/auth/get`
    """

    account: AccountBase
    numbers: ProcessorNumber
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

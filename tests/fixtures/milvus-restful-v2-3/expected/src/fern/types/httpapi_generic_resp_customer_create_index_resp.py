

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customer_create_index_resp import CustomerCreateIndexResp


class HttpapiGenericRespCustomerCreateIndexResp(UniversalBaseModel):
    code: typing.Optional[int] = None
    data: typing.Optional[CustomerCreateIndexResp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

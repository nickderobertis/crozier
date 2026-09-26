

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .httpapi_generic_resp_customer_upsert_resp_data import HttpapiGenericRespCustomerUpsertRespData


class HttpapiGenericRespCustomerUpsertResp(UniversalBaseModel):
    code: typing.Optional[int] = None
    data: typing.Optional[HttpapiGenericRespCustomerUpsertRespData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

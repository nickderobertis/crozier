

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_employment_item import CreditEmploymentItem
from .request_id import RequestId


class CreditEmploymentGetResponse(UniversalBaseModel):
    """
    CreditEmploymentGetResponse defines the response schema for `/credit/employment/get`.
    """

    items: typing.List[CreditEmploymentItem] = pydantic.Field()
    """
    Array of employment items.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

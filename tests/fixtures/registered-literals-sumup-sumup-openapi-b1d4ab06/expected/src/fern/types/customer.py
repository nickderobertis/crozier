

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .personal_details import PersonalDetails


class Customer(UniversalBaseModel):
    """
    Saved customer details.
    """

    customer_id: str = pydantic.Field()
    """
    Unique identifier of the customer.
    """

    personal_details: typing.Optional[PersonalDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

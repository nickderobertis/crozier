

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .email import Email
from .phone_number import PhoneNumber


class LinkedEcommerceCustomer(UniversalBaseModel):
    """
    The customer this entity is linked to.
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company name of the customer
    """

    emails: typing.Optional[typing.List[Email]] = None
    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First name of the customer
    """

    id: str = pydantic.Field()
    """
    The ID of the customer this entity is linked to.
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last name of the customer
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the customer
    """

    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

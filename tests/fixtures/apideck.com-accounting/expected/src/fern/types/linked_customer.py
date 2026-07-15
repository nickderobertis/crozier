

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkedCustomer(UniversalBaseModel):
    """
    The customer this entity is linked to.
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company name of the customer.
    """

    display_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display ID of the customer.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name of the customer.
    """

    id: str = pydantic.Field()
    """
    The ID of the customer this entity is linked to.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the customer. Deprecated, use display_name instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

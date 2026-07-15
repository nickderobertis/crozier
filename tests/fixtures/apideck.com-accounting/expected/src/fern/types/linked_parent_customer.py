

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkedParentCustomer(UniversalBaseModel):
    """
    The parent customer this entity is linked to.
    """

    id: str = pydantic.Field()
    """
    The parent ID of the customer this entity is linked to.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the parent customer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreditSessionItemAddResult(UniversalBaseModel):
    """
    The details of an Item add in Link.
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Institution ID associated with the Item.
    """

    item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive.
    """

    public_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Returned once a user has successfully linked their Item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

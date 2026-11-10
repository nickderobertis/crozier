

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .counterparty_type import CounterpartyType


class Counterparty(UniversalBaseModel):
    """
    The counterparty, such as the merchant or financial institution, is extracted by Plaid from the raw description.
    """

    entity_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique, stable, Plaid-generated id that maps to the counterparty.
    """

    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of a logo associated with the counterparty, if available. The logo is formatted as a 100x100 pixel PNG file.
    """

    name: str = pydantic.Field()
    """
    The name of the counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description.
    """

    type: CounterpartyType
    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website associated with the counterparty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

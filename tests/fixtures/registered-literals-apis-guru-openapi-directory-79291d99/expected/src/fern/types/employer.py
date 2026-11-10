

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address_data_nullable import AddressDataNullable


class Employer(UniversalBaseModel):
    """
    Data about the employer.
    """

    address: typing.Optional[AddressDataNullable] = None
    confidence_score: float = pydantic.Field()
    """
    A number from 0 to 1 indicating Plaid's level of confidence in the pairing between the employer and the institution (not yet implemented).
    """

    employer_id: str = pydantic.Field()
    """
    Plaid's unique identifier for the employer.
    """

    name: str = pydantic.Field()
    """
    The name of the employer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

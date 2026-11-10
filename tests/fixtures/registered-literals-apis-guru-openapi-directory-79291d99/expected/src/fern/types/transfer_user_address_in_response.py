

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferUserAddressInResponse(UniversalBaseModel):
    """
    The address associated with the account holder.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ex. "San Francisco"
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    A two-letter country code (e.g., "US").
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code (e.g., "94103").
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state or province (e.g., "CA").
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    The street number and name (i.e., "100 Market St.").
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

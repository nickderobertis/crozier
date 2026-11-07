

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .country_code import CountryCode


class Address(UniversalBaseModel):
    """
    An address somewhere in the world. The address fields used depend on the country conventions. For example, in Great Britain, `city` is `post_town`. In the United States, the top-level administrative unit used in addresses is `state`, whereas in Chile it's `region`.
    Whether an address is valid or not depends on whether the locally required fields are present. Fields not supported in a country will be ignored.
    """

    street_address: typing.Optional[typing.List[str]] = None
    post_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code (aka. zip code) of the address.
    """

    country: CountryCode
    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city of the address.
    """

    province: typing.Optional[str] = pydantic.Field(default=None)
    """
    The province where the address is located. This may not be relevant in some countries.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region where the address is located. This may not be relevant in some countries.
    """

    county: typing.Optional[str] = pydantic.Field(default=None)
    """
    A county is a geographic region of a country used for administrative or other purposes in some nations. Used in countries such as Ireland, Romania, etc.
    """

    autonomous_community: typing.Optional[str] = pydantic.Field(default=None)
    """
    In Spain, an autonomous community is the first sub-national level of political and administrative division.
    """

    post_town: typing.Optional[str] = pydantic.Field(default=None)
    """
    A post town is a required part of all postal addresses in the United Kingdom and Ireland, and a basic unit of the postal delivery system.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    Most often, a country has a single state, with various administrative divisions. The term "state" is sometimes used to refer to the federated polities that make up the federation. Used in countries such as the United States and Brazil.
    """

    neighborhood: typing.Optional[str] = pydantic.Field(default=None)
    """
    Locality level of the address. Used in countries such as Brazil or Chile.
    """

    commune: typing.Optional[str] = pydantic.Field(default=None)
    """
    In many countries, terms cognate with "commune" are used, referring to the community living in the area and the common interest. Used in countries such as Chile.
    """

    department: typing.Optional[str] = pydantic.Field(default=None)
    """
    A department (French: département, Spanish: departamento) is an administrative or political division in several countries. Used in countries such as Colombia.
    """

    municipality: typing.Optional[str] = pydantic.Field(default=None)
    """
    A municipality is usually a single administrative division having corporate status and powers of self-government or jurisdiction as granted by national and regional laws to which it is subordinate. Used in countries such as Colombia.
    """

    district: typing.Optional[str] = pydantic.Field(default=None)
    """
    A district is a type of administrative division that in some countries is managed by the local government. Used in countries such as Portugal.
    """

    zip_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    A US system of postal codes used by the United States Postal Service (USPS).
    """

    eircode: typing.Optional[str] = pydantic.Field(default=None)
    """
    A postal address in Ireland.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

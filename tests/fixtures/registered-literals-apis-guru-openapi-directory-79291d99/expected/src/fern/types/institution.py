

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .auth_metadata import AuthMetadata
from .country_code import CountryCode
from .institution_status import InstitutionStatus
from .payment_initiation_metadata import PaymentInitiationMetadata
from .products import Products


class Institution(UniversalBaseModel):
    """
    Details relating to a specific financial institution
    """

    auth_metadata: typing.Optional[AuthMetadata] = None
    country_codes: typing.List[CountryCode] = pydantic.Field()
    """
    A list of the country codes supported by the institution.
    """

    dtc_numbers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A partial list of DTC numbers associated with the institution.
    """

    institution_id: str = pydantic.Field()
    """
    Unique identifier for the institution
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64 encoded representation of the institution's logo, returned as a base64 encoded 152x152 PNG. Not all institutions' logos are available.
    """

    name: str = pydantic.Field()
    """
    The official name of the institution
    """

    oauth: bool = pydantic.Field()
    """
    Indicates that the institution has a mandatory OAuth login flow. Note that `oauth` may be `false` even for institutions that support OAuth, if the institution is in the process of migrating to OAuth and some active Items still exist that do not use OAuth.
    """

    payment_initiation_metadata: typing.Optional[PaymentInitiationMetadata] = None
    primary_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hexadecimal representation of the primary color used by the institution
    """

    products: typing.List[Products] = pydantic.Field()
    """
    A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return `auth` in the product array; institutions that do not list `auth` may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the `auth_metadata` object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/).
    """

    routing_numbers: typing.List[str] = pydantic.Field()
    """
    A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution.
    """

    status: typing.Optional[InstitutionStatus] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the institution's website
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

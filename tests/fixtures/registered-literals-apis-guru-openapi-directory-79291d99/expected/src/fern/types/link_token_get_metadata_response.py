

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_filters_response import AccountFiltersResponse
from .country_code import CountryCode
from .link_token_create_institution_data import LinkTokenCreateInstitutionData
from .products import Products


class LinkTokenGetMetadataResponse(UniversalBaseModel):
    """
    An object specifying the arguments originally provided to the `/link/token/create` call.
    """

    account_filters: typing.Optional[AccountFiltersResponse] = None
    client_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `client_name` specified in the `/link/token/create` call.
    """

    country_codes: typing.List[CountryCode] = pydantic.Field()
    """
    The `country_codes` specified in the `/link/token/create` call.
    """

    initial_products: typing.List[Products] = pydantic.Field()
    """
    The `products` specified in the `/link/token/create` call.
    """

    institution_data: typing.Optional[LinkTokenCreateInstitutionData] = None
    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `language` specified in the `/link/token/create` call.
    """

    redirect_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `redirect_uri` specified in the `/link/token/create` call.
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `webhook` specified in the `/link/token/create` call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

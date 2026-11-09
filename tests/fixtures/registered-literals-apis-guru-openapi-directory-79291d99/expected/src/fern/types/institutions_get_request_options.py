

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .products import Products


class InstitutionsGetRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/institutions/get` results.
    """

    include_auth_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, returns metadata related to the Auth product indicating which auth methods are supported.
    """

    include_optional_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, return the institution's homepage URL, logo and primary brand color.
    
    Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.
    """

    include_payment_initiation_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported.
    """

    oauth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Limit results to institutions with or without mandatory OAuth login flows. Note that institutions will only have `oauth` set to `true` if *all* Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth may have the `oauth` attribute set to `false` even if they support OAuth.
    """

    products: typing.Optional[typing.List[Products]] = pydantic.Field(default=None)
    """
    Filter the Institutions based on which products they support. 
    """

    routing_numbers: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .institutions_search_payment_initiation_options import InstitutionsSearchPaymentInitiationOptions


class InstitutionsSearchRequestOptions(UniversalBaseModel):
    """
    An optional object to filter `/institutions/search` results.
    """

    include_auth_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, returns metadata related to the Auth product indicating which auth methods are supported.
    """

    include_optional_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When true, return the institution's homepage URL, logo and primary brand color.
    """

    include_payment_initiation_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported.
    """

    oauth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Limit results to institutions with or without mandatory OAuth login flows. Note that institutions will only have `oauth` set to `true` if *all* Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth may have the `oauth` attribute set to `false` even if they support OAuth.
    """

    payment_initiation: typing.Optional[InstitutionsSearchPaymentInitiationOptions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plaid_error_type import PlaidErrorType


class PlaidError(UniversalBaseModel):
    """
    We use standard HTTP response codes for success and failure notifications, and our errors are further classified by `error_type`. In general, 200 HTTP codes correspond to success, 40X codes are for developer- or user-related failures, and 50X codes are for Plaid-related issues. An Item with a non-`null` error object will only be part of an API response when calling `/item/get` to view Item status. Otherwise, error fields will be `null` if no error has occurred; if an error has occurred, an error code will be returned instead.
    """

    causes: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    In the Assets product, a request can pertain to more than one Item. If an error is returned for such a request, `causes` will return an array of errors containing a breakdown of these errors on the individual Item level, if any can be identified.
    
    `causes` will only be provided for the `error_type` `ASSET_REPORT_ERROR`. `causes` will also not be populated inside an error nested within a `warning` object.
    """

    display_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A user-friendly representation of the error code. `null` if the error is not related to user action.
    
    This may change over time and is not safe for programmatic use.
    """

    documentation_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of a Plaid documentation page with more information about the error
    """

    error_code: str = pydantic.Field()
    """
    The particular error code. Safe for programmatic use.
    """

    error_message: str = pydantic.Field()
    """
    A developer-friendly representation of the error code. This may change over time and is not safe for programmatic use.
    """

    error_type: PlaidErrorType
    request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID identifying the request, to be used for troubleshooting purposes. This field will be omitted in errors provided by webhooks.
    """

    status: typing.Optional[float] = pydantic.Field(default=None)
    """
    The HTTP status code associated with the error. This will only be returned in the response body when the error information is provided via a webhook.
    """

    suggested_action: typing.Optional[str] = pydantic.Field(default=None)
    """
    Suggested steps for resolving the error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

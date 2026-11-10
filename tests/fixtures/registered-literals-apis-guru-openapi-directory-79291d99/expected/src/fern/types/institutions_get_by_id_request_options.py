

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstitutionsGetByIdRequestOptions(UniversalBaseModel):
    """
    Specifies optional parameters for `/institutions/get_by_id`. If provided, must not be `null`.
    """

    include_auth_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, returns metadata related to the Auth product indicating which auth methods are supported.
    """

    include_optional_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, return an institution's logo, brand color, and URL. When available, the bank's logo is returned as a base64 encoded 152x152 PNG, the brand color is in hexadecimal format. The default value is `false`.
    
    Note that Plaid does not own any of the logos shared by the API and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos.
    """

    include_payment_initiation_metadata: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, returns metadata related to the Payment Initiation product indicating which payment configurations are supported.
    """

    include_status: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, the response will include status information about the institution. Default value is `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

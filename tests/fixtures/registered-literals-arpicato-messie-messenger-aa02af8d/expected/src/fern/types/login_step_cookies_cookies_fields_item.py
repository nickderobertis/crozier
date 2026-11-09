

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_cookies_cookies_fields_item_type import LoginStepCookiesCookiesFieldsItemType


class LoginStepCookiesCookiesFieldsItem(UniversalBaseModel):
    """
    An individual cookie or other stored data item that must be extracted.
    """

    type: LoginStepCookiesCookiesFieldsItemType = pydantic.Field()
    """
    The type of data to extract.
    """

    name: str = pydantic.Field()
    """
    The name of the item to extract.
    """

    request_url_regex: typing.Optional[str] = pydantic.Field(default=None)
    """
    For the `request_header` and `request_body` types, a regex that matches the URLs from which the values can be extracted.
    """

    cookie_domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    For the `cookie` type, the domain of the cookie.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

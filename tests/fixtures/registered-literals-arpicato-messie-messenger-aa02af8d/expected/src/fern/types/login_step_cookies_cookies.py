

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_cookies_cookies_fields_item import LoginStepCookiesCookiesFieldsItem


class LoginStepCookiesCookies(UniversalBaseModel):
    """
    Parameters for the cookie login step
    """

    url: str = pydantic.Field()
    """
    The URL to open when using a webview to extract cookies.
    """

    user_agent: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional user agent that the webview should use.
    """

    wait_for_url_pattern: typing.Optional[str] = pydantic.Field(default=None)
    """
    A regex pattern that the URL should match before the client closes the webview.
    
    The client may submit the login if the user closes the webview after all cookies are collected
    even if this URL is not reached, but it should only automatically close the webview after
    both cookies and the URL match.
    """

    extract_js: typing.Optional[str] = pydantic.Field(default=None)
    """
    A JavaScript snippet that can extract some or all of the fields.
    The snippet will evaluate to a promise that resolves when the relevant fields are found.
    Fields that are not present in the promise result must be extracted another way.
    """

    fields: typing.List[LoginStepCookiesCookiesFieldsItem] = pydantic.Field()
    """
    The list of cookies or other stored data that must be extracted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

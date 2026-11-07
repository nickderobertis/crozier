

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .login_step_complete_complete import LoginStepCompleteComplete
from .login_step_cookies_cookies import LoginStepCookiesCookies
from .login_step_display_and_wait_display_and_wait import LoginStepDisplayAndWaitDisplayAndWait
from .login_step_user_input_user_input import LoginStepUserInputUserInput


class Base(UniversalBaseModel):
    login_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier for the current login process. Must be passed to execute more steps of the login.
    """

    step_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An unique ID identifying this step. This can be used to implement special behavior in clients.
    """

    instructions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable instructions for completing this login step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LoginStep_DisplayAndWait(Base):
    """
    A step in a login process.
    """

    type: typing.Literal["display_and_wait"] = "display_and_wait"
    display_and_wait: LoginStepDisplayAndWaitDisplayAndWait

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LoginStep_UserInput(Base):
    """
    A step in a login process.
    """

    type: typing.Literal["user_input"] = "user_input"
    user_input: LoginStepUserInputUserInput

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LoginStep_Cookies(Base):
    """
    A step in a login process.
    """

    type: typing.Literal["cookies"] = "cookies"
    cookies: LoginStepCookiesCookies

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LoginStep_Complete(Base):
    """
    A step in a login process.
    """

    type: typing.Literal["complete"] = "complete"
    complete: LoginStepCompleteComplete

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LoginStep = typing_extensions.Annotated[
    typing.Union[LoginStep_DisplayAndWait, LoginStep_UserInput, LoginStep_Cookies, LoginStep_Complete],
    pydantic.Field(discriminator="type"),
]

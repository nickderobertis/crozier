

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HooksFilter(UniversalBaseModel):
    """
    User specific hook overrides
    """

    external_auth_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the external auth hook, if defined, will not be executed
    """

    pre_login_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the pre-login hook, if defined, will not be executed
    """

    check_password_disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, the check password hook, if defined, will not be executed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

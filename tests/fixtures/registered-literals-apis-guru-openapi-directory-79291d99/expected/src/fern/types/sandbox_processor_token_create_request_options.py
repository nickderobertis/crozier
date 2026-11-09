

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_override_password import SandboxOverridePassword
from .sandbox_override_username import SandboxOverrideUsername


class SandboxProcessorTokenCreateRequestOptions(UniversalBaseModel):
    """
    An optional set of options to be used when configuring the Item. If specified, must not be `null`.
    """

    override_password: typing.Optional[SandboxOverridePassword] = None
    override_username: typing.Optional[SandboxOverrideUsername] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

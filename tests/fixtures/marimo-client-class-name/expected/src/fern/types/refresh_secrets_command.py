

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .refresh_secrets_command_type import RefreshSecretsCommandType


class RefreshSecretsCommand(UniversalBaseModel):
    """
    Refresh secrets from the secrets store.

        Reloads secrets from the provider without restarting the kernel.
    """

    type: RefreshSecretsCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

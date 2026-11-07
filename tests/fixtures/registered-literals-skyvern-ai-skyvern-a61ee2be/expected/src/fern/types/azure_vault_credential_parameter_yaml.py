

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AzureVaultCredentialParameterYaml(UniversalBaseModel):
    key: str
    description: typing.Optional[str] = None
    vault_name: str
    username_key: str
    password_key: str
    totp_secret_key: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

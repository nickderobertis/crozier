

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sandbox_environment_secret import SandboxEnvironmentSecret


class SandboxEnvironmentNetworking(UniversalBaseModel):
    domain_allow_list: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma-separated allowed domains.
    """

    network_block_all: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Block all outbound network access. When true, domain_allow_list and secrets are not used.
    """

    secrets: typing.Optional[typing.List[SandboxEnvironmentSecret]] = pydantic.Field(default=None)
    """
    Network-scoped secrets.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

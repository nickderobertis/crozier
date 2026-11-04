

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SandboxEnvironmentSecret(UniversalBaseModel):
    env: str = pydantic.Field()
    """
    Environment variable name injected into the sandbox.
    """

    hosts: typing.List[str] = pydantic.Field()
    """
    Hosts this secret may be sent to.
    """

    value: str = pydantic.Field()
    """
    Secret value; GET responses use a redacted stand-in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

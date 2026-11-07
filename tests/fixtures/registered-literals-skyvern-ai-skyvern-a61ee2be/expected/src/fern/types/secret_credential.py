

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SecretCredential(UniversalBaseModel):
    """
    Generic secret credential.
    """

    secret_value: str = pydantic.Field()
    """
    The secret value
    """

    secret_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional label describing the secret
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

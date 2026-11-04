

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SecretCredentialResponse(UniversalBaseModel):
    """
    Response model for secret credentials — non-sensitive fields only.

    SECURITY: Must NEVER include the secret_value.
    """

    secret_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional label for the stored secret
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

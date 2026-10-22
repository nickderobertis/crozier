

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImpersonationToken(UniversalBaseModel):
    impersonation_token: str = pydantic.Field()
    """
    The Impersonation token.
    """

    token_type: str = pydantic.Field()
    """
    Token type.
    """

    expires_in: float = pydantic.Field()
    """
    Token expiration time.
    """

    context: str = pydantic.Field()
    """
    the Impersonation token context.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

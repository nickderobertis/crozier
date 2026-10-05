

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Secret(UniversalBaseModel):
    """
    Reference to a secret stored in a secret manager.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specific field within the secret
    """

    path: str = pydantic.Field()
    """
    Path to the secret
    """

    secret_manager_url: str = pydantic.Field()
    """
    Secret Manager URL
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    Version of the secret
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

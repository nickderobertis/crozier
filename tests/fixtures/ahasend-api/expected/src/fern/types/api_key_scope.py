

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApiKeyScope(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the scope
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the scope was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the scope was last updated
    """

    api_key_id: str = pydantic.Field()
    """
    ID of the API key this scope belongs to
    """

    scope: str = pydantic.Field()
    """
    The scope string
    """

    domain_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Domain ID for domain-specific scopes; always present and null for non-domain scopes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

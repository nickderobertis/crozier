

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Environment(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the environment
    """

    org_id: str = pydantic.Field()
    """
    Unique identifier for the organization that the environment belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the environment
    """

    slug: str = pydantic.Field()
    """
    A url-friendly, unique identifier for the environment within an organization
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the environment
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of environment creation
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of environment deletion, or null if the environment is still active
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AiSecret(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the AI secret
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of AI secret creation
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of last AI secret update
    """

    org_id: str = pydantic.Field()
    """
    Unique identifier for the organization
    """

    name: str = pydantic.Field()
    """
    Name of the AI secret
    """

    type: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    preview_secret: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

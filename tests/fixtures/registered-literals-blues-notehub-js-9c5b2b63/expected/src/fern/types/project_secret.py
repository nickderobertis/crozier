

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectSecret(UniversalBaseModel):
    """
    Metadata for a project secret. The value is never returned.
    """

    created: dt.datetime = pydantic.Field()
    """
    When the secret was first created.
    """

    created_by: str = pydantic.Field()
    """
    The actor who created the secret.
    """

    modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the secret was last updated.
    """

    modified_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The actor who last updated the secret.
    """

    name: str = pydantic.Field()
    """
    The secret name (alphanumeric and underscores only).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

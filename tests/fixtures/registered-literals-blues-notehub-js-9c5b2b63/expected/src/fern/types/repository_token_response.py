

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RepositoryTokenResponse(UniversalBaseModel):
    database: str = pydantic.Field()
    """
    Storage service database name scoped to this repository
    """

    expires_at: dt.datetime = pydantic.Field()
    """
    Absolute expiration time of the ephemeral user. The storage
    service will reject connections and queries after this instant.
    """

    host: str = pydantic.Field()
    """
    Storage service hostname the caller should connect to
    """

    password: str = pydantic.Field()
    """
    Ephemeral password. Returned once; not stored by Notehub. Hold
    this in memory only and discard after `expires_at`.
    """

    port: int = pydantic.Field()
    """
    Storage service port
    """

    username: str = pydantic.Field()
    """
    Ephemeral storage service username (prefixed with `u_`)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ProjectWithDatabaseResponseOutputDatabase(UniversalBaseModel):
    host: str = pydantic.Field()
    """
    Database host
    """

    version: str = pydantic.Field()
    """
    Database version
    """

    postgres_engine: str = pydantic.Field()
    """
    Database engine
    """

    release_channel: str = pydantic.Field()
    """
    Release channel
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

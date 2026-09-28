

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ResourcesSyncPostResponseData(UniversalBaseModel):
    upserted: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of resources upserted
    """

    deleted: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of resources deleted
    """

    healthy: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Health check result
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Operation message
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

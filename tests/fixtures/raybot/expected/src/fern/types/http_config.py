

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HttpConfig(UniversalBaseModel):
    port: int = pydantic.Field()
    """
    The port for the HTTP server
    """

    swagger: bool = pydantic.Field()
    """
    Whether to enable the Swagger UI
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

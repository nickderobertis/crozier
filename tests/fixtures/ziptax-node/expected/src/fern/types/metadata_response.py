

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataResponse(UniversalBaseModel):
    go_version: str = pydantic.Field()
    """
    Go runtime version the running binary was built with.
    """

    hostname: str = pydantic.Field()
    """
    Hostname of the instance serving the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

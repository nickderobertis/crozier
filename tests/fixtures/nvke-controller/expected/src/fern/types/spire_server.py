

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SpireServer(UniversalBaseModel):
    """
    A SPIRE server address the cluster's SPIRE agents dial.
    """

    address: str = pydantic.Field()
    """
    Host name or IP address of the SPIRE server.
    """

    port: int = pydantic.Field()
    """
    SPIRE server port.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CloudConfig(UniversalBaseModel):
    enable: bool = pydantic.Field()
    """
    Whether to enable the cloud service
    """

    address: str = pydantic.Field()
    """
    The address for the cloud service
    """

    token: str = pydantic.Field()
    """
    The token for the cloud service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LargeToolResponseConfig(UniversalBaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Offload oversized tool responses to a sandbox file. Default: true.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

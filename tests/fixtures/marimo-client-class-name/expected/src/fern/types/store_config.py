

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .store_config_type import StoreConfigType


class StoreConfig(UniversalBaseModel):
    """
    Configuration for a single cache store.
    """

    args: typing.Optional[typing.Dict[str, typing.Any]] = None
    type: typing.Optional[StoreConfigType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

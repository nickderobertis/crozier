

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_id import DataId
from .data_provider_id import DataProviderId


class PrivateData(UniversalBaseModel):
    """
    Description of the exact private data
    """

    private_data: DataId
    data_provider: DataProviderId
    uri: str = pydantic.Field()
    """
    Location description of the private data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

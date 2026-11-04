

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mscid import Mscid
from .uri import Uri


class DataType(UniversalBaseModel):
    mscid: typing.Optional[Mscid] = None
    uri: typing.Optional[Uri] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL identifying this type of data.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Descriptor for this type of data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

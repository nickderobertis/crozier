

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .properties import Properties


class EditableMetaData(UniversalBaseModel):
    """ """

    description: typing.Optional[str] = None
    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    
    """

    name: typing.Optional[str] = None
    properties: typing.Optional[Properties] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

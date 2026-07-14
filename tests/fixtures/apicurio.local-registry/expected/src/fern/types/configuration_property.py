

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigurationProperty(UniversalBaseModel):
    """ """

    description: str = pydantic.Field()
    """
    
    """

    label: str = pydantic.Field()
    """
    
    """

    name: str
    type: str = pydantic.Field()
    """
    
    """

    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

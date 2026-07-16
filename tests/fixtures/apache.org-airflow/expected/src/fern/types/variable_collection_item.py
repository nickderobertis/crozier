

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VariableCollectionItem(UniversalBaseModel):
    """
    XCom entry collection item.
    The value field are only available when retrieving a single object due to the sensitivity of this data.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the variable.
    
    *New in version 2.4.0*
    """

    key: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

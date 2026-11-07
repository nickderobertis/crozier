

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataSetField(UniversalBaseModel):
    datatype: typing.Optional[int] = pydantic.Field(default=None)
    """
    The datatype of the field
    """

    jsonata: typing.Optional[str] = pydantic.Field(default=None)
    """
    the JSONata expression used to populate this field
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

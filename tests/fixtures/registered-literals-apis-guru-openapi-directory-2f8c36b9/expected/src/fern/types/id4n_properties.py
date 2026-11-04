

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Id4NProperties(UniversalBaseModel):
    """
    An id4n with its properties
    """

    id4n: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID4n
    """

    properties: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The properties of the ID4n
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

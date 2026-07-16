

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Filtering(UniversalBaseModel):
    exclude: typing.Optional[typing.List[typing.Dict[str, str]]] = pydantic.Field(default=None)
    """
    Excluding pattern
    """

    include: typing.Optional[typing.List[typing.Dict[str, str]]] = pydantic.Field(default=None)
    """
    Including pattern
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

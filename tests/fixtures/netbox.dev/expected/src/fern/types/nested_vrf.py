

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NestedVrf(UniversalBaseModel):
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    name: str
    prefix_count: typing.Optional[int] = None
    rd: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique route distinguisher (as defined in RFC 4364)
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

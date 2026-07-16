

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NestedUser(UniversalBaseModel):
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    url: typing.Optional[str] = None
    username: str = pydantic.Field()
    """
    Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

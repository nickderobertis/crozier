

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QueryField(UniversalBaseModel):
    module: str
    category: str
    field: str
    visits: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The visit labels for this field for session-level data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

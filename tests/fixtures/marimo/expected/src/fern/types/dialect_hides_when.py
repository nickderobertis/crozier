

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dialect_hides_when_kind import DialectHidesWhenKind


class DialectHidesWhen(UniversalBaseModel):
    """
    Hide this suggestion when a live SQL engine dialect contains a substring.
    """

    kind: DialectHidesWhenKind
    substrings: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

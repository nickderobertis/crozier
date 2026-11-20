

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchHit(UniversalBaseModel):
    """
    One /search result: the dataset + WHY it matched (name / namespace / tag:* / column:*).
    """

    matches: typing.Optional[typing.List[str]] = None
    name: str
    namespace: typing.Optional[str] = None
    tags: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

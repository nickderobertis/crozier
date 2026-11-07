

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FrequentwordTypeCustomCustom(UniversalBaseModel):
    """
    Custom frequent words
    """

    terms: typing.List[str] = pydantic.Field()
    """
    List of frequent terms, max. 256 terms.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

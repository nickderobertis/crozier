

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetLinksExpandResponseSplitUrlv2Item(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    Split URL destination
    """

    percent: int = pydantic.Field()
    """
    Traffic percentage
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

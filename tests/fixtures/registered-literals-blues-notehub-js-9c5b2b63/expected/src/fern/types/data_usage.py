

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataUsage(UniversalBaseModel):
    kb_remaining: float = pydantic.Field()
    """
    Kilobytes remaining in the plan
    """

    kb_total: float = pydantic.Field()
    """
    Total Kilobytes included in the plan
    """

    kb_used: float = pydantic.Field()
    """
    Kilobytes used to date
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

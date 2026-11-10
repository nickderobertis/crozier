

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SummarizationResponseSummarization(UniversalBaseModel):
    summary: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field()
    """
    Array of summaries.
    """

    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

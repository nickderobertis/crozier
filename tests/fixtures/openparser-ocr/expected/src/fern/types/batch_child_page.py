

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .batch_child_summary import BatchChildSummary


class BatchChildPage(UniversalBaseModel):
    items: typing.List[BatchChildSummary]
    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present when more child summaries are available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

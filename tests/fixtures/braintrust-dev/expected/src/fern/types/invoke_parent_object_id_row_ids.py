

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvokeParentObjectIdRowIds(UniversalBaseModel):
    """
    Identifiers for the row to to log a subspan under
    """

    id: str = pydantic.Field()
    """
    The id of the row
    """

    span_id: str = pydantic.Field()
    """
    The span_id of the row
    """

    root_span_id: str = pydantic.Field()
    """
    The root_span_id of the row
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

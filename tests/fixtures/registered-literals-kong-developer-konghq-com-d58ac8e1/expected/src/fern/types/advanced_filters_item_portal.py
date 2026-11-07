

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .requests_filter_type import RequestsFilterType
from .unscoped_uuid import UnscopedUuid


class AdvancedFiltersItemPortal(UniversalBaseModel):
    operator: RequestsFilterType
    value: typing.Optional[typing.List[UnscopedUuid]] = pydantic.Field(default=None)
    """
    The IDs to include in the results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

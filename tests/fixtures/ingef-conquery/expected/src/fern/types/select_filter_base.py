

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .column_id import ColumnId
from .filter_base import FilterBase
from .searchable import Searchable
from .template_id import TemplateId


class SelectFilterBase(FilterBase, Searchable):
    """
    Filters events for a user defined list of values in a specific column.
    """

    column: typing.Optional[ColumnId] = None
    labels: typing.Optional[typing.Dict[str, str]] = None
    template: typing.Optional[TemplateId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

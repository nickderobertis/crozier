

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_history_execution_status_time_stratified_infos_item_years_item_quarters_item import (
    EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItemQuartersItem,
)


class EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItem(UniversalBaseModel):
    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    The year of the entries.
    """

    values: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Aggregated values for the whole year.
    """

    quarters: typing.Optional[typing.List[EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItemQuartersItem]] = (
        pydantic.Field(default=None)
    )
    """
    For each contained quarter an entry also containing the aggregated values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

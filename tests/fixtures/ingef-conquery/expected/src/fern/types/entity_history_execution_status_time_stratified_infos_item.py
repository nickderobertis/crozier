

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_history_execution_status_time_stratified_infos_item_columns import (
    EntityHistoryExecutionStatusTimeStratifiedInfosItemColumns,
)
from .entity_history_execution_status_time_stratified_infos_item_years_item import (
    EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItem,
)


class EntityHistoryExecutionStatusTimeStratifiedInfosItem(UniversalBaseModel):
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display label of the group of Selects.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Detailed description of the selects.
    """

    columns: typing.Optional[EntityHistoryExecutionStatusTimeStratifiedInfosItemColumns] = pydantic.Field(default=None)
    """
    Description of the columns of totals, years and quarters.
    """

    totals: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Values for the entire observation period.
    """

    years: typing.Optional[typing.List[EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItem]] = pydantic.Field(
        default=None
    )
    """
    One entry for each year, containing the values aggregated for each year and its quarters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .eval_status_page_config_sort_order import EvalStatusPageConfigSortOrder


class EvalStatusPageConfig(UniversalBaseModel):
    """
    Configuration for what data to display
    """

    score_columns: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The score columns to display on the page
    """

    metric_columns: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The metric columns to display on the page
    """

    grouping_field: typing.Optional[str] = pydantic.Field(default=None)
    """
    The metadata field to use for grouping experiments (model)
    """

    filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    BTQL filter to apply to experiment data
    """

    sort_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    Field to sort results by (format: 'score:<name>' or 'metric:<name>')
    """

    sort_order: typing.Optional[EvalStatusPageConfigSortOrder] = pydantic.Field(default=None)
    """
    Sort order (ascending or descending)
    """

    api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    The API key used for fetching experiment data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

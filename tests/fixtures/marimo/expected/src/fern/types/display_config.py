

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .display_config_cell_output import DisplayConfigCellOutput
from .display_config_dataframes import DisplayConfigDataframes
from .display_config_default_width import DisplayConfigDefaultWidth
from .display_config_theme import DisplayConfigTheme


class DisplayConfig(UniversalBaseModel):
    """
    Configuration for display.

        **Keys.**

        - `theme`: `"light"`, `"dark"`, or `"system"`
        - `code_editor_font_size`: font size for the code editor
        - `cell_output`: `"above"` or `"below"`
        - `dataframes`: `"rich"` or `"plain"`
        - `custom_css`: list of paths to custom CSS files
        - `default_table_page_size`: default number of rows to display in tables
        - `default_table_max_columns`: default maximum number of columns to display in tables
        - `reference_highlighting`: if `True`, highlight reactive variable references
        - `code_lens`: if `True`, show inline icons in cell editors linking
          datasources, storage buckets, and caches to their panels
        - `locale`: locale for date formatting and internationalization (e.g., "en-US", "en-GB", "de-DE")
    """

    cell_output: DisplayConfigCellOutput
    code_editor_font_size: int
    code_lens: typing.Optional[bool] = None
    custom_css: typing.Optional[typing.List[str]] = None
    dataframes: DisplayConfigDataframes
    default_table_max_columns: int
    default_table_page_size: int
    default_width: DisplayConfigDefaultWidth
    locale: typing.Optional[str] = None
    reference_highlighting: typing.Optional[bool] = None
    theme: DisplayConfigTheme

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

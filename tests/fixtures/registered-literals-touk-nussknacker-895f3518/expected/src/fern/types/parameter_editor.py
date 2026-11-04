

import typing

from .bool_parameter_editor import BoolParameterEditor
from .cron_parameter_editor import CronParameterEditor
from .date_parameter_editor import DateParameterEditor
from .date_time_parameter_editor import DateTimeParameterEditor
from .dict_parameter_editor import DictParameterEditor
from .duration_parameter_editor import DurationParameterEditor
from .fixed_values_parameter_editor import FixedValuesParameterEditor
from .fixed_values_with_icon_parameter_editor import FixedValuesWithIconParameterEditor
from .fixed_values_with_radio_parameter_editor import FixedValuesWithRadioParameterEditor
from .json_parameter_editor import JsonParameterEditor
from .json_template_parameter_editor import JsonTemplateParameterEditor
from .multi_select_editor import MultiSelectEditor
from .period_parameter_editor import PeriodParameterEditor
from .spel_parameter_editor import SpelParameterEditor
from .spel_template_parameter_editor import SpelTemplateParameterEditor
from .sql_parameter_editor import SqlParameterEditor
from .tabular_typed_data_editor import TabularTypedDataEditor
from .textarea_parameter_editor import TextareaParameterEditor
from .time_parameter_editor import TimeParameterEditor

ParameterEditor = typing.Union[
    BoolParameterEditor,
    CronParameterEditor,
    DateParameterEditor,
    DateTimeParameterEditor,
    DictParameterEditor,
    DurationParameterEditor,
    FixedValuesParameterEditor,
    FixedValuesWithIconParameterEditor,
    FixedValuesWithRadioParameterEditor,
    JsonParameterEditor,
    JsonTemplateParameterEditor,
    MultiSelectEditor,
    PeriodParameterEditor,
    SpelParameterEditor,
    SpelTemplateParameterEditor,
    SqlParameterEditor,
    TabularTypedDataEditor,
    TextareaParameterEditor,
    TimeParameterEditor,
]

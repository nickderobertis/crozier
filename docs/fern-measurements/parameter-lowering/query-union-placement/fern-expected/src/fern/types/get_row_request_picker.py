

import typing

from .get_row_request_picker_one import GetRowRequestPickerOne
from .get_row_request_picker_zero import GetRowRequestPickerZero

GetRowRequestPicker = typing.Union[GetRowRequestPickerZero, GetRowRequestPickerOne]

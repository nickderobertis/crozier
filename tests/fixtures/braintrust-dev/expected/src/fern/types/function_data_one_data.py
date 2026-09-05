

import typing

from .function_data_one_data_code import FunctionDataOneDataCode
from .function_data_one_data_zero import FunctionDataOneDataZero

FunctionDataOneData = typing.Union[FunctionDataOneDataZero, FunctionDataOneDataCode]

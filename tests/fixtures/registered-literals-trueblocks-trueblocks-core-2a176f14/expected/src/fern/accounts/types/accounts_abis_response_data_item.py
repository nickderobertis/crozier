

import typing

from ...types.abi import Abi
from ...types.function import Function
from ...types.parameter import Parameter

AccountsAbisResponseDataItem = typing.Union[Abi, Function, Parameter]

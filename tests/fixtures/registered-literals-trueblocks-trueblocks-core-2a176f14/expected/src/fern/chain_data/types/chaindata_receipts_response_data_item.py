

import typing

from ...types.function import Function
from ...types.parameter import Parameter
from ...types.receipt import Receipt

ChaindataReceiptsResponseDataItem = typing.Union[Function, Parameter, Receipt]

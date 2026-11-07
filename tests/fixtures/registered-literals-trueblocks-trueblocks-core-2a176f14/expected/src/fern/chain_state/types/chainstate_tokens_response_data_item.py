

import typing

from ...types.approval import Approval
from ...types.token import Token

ChainstateTokensResponseDataItem = typing.Union[Approval, Token]

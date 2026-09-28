

import typing

from .key_to_multi_value_key_match_style import KeyToMultiValueKeyMatchStyle
from .key_to_multi_value_zero_item import KeyToMultiValueZeroItem

KeyToMultiValue = typing.Union[typing.List[KeyToMultiValueZeroItem], KeyToMultiValueKeyMatchStyle]

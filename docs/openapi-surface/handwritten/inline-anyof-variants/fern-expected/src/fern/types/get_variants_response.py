

import typing

from .get_variants_response_four import GetVariantsResponseFour
from .get_variants_response_one_item import GetVariantsResponseOneItem
from .get_variants_response_three_item import GetVariantsResponseThreeItem
from .get_variants_response_two_item import GetVariantsResponseTwoItem
from .get_variants_response_zero import GetVariantsResponseZero

GetVariantsResponse = typing.Union[
    GetVariantsResponseZero,
    typing.List[GetVariantsResponseOneItem],
    typing.List[GetVariantsResponseTwoItem],
    typing.List[GetVariantsResponseThreeItem],
    GetVariantsResponseFour,
    typing.List[typing.Optional[str]],
    typing.List[typing.Optional[int]],
]

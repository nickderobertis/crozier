

import typing

from .get_variants_response_five import GetVariantsResponseFive
from .get_variants_response_four_item import GetVariantsResponseFourItem
from .get_variants_response_one import GetVariantsResponseOne
from .get_variants_response_seven_item import GetVariantsResponseSevenItem
from .get_variants_response_three_item import GetVariantsResponseThreeItem
from .get_variants_response_two_item import GetVariantsResponseTwoItem
from .get_variants_response_zero import GetVariantsResponseZero

GetVariantsResponse = typing.Union[
    GetVariantsResponseZero,
    GetVariantsResponseOne,
    typing.List[GetVariantsResponseTwoItem],
    typing.List[GetVariantsResponseThreeItem],
    typing.List[GetVariantsResponseFourItem],
    GetVariantsResponseFive,
    typing.List[typing.Optional[str]],
    typing.List[GetVariantsResponseSevenItem],
    typing.Dict[str, typing.Any],
]

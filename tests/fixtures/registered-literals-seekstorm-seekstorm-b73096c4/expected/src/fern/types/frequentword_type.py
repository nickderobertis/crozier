

import typing

from .frequentword_type_custom import FrequentwordTypeCustom
from .frequentword_type_four import FrequentwordTypeFour
from .frequentword_type_one import FrequentwordTypeOne
from .frequentword_type_three import FrequentwordTypeThree
from .frequentword_type_two import FrequentwordTypeTwo
from .frequentword_type_zero import FrequentwordTypeZero

FrequentwordType = typing.Union[
    FrequentwordTypeZero,
    FrequentwordTypeOne,
    FrequentwordTypeTwo,
    FrequentwordTypeThree,
    FrequentwordTypeFour,
    FrequentwordTypeCustom,
]

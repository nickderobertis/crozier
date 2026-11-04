

import typing

from .stopword_type_custom import StopwordTypeCustom
from .stopword_type_four import StopwordTypeFour
from .stopword_type_one import StopwordTypeOne
from .stopword_type_three import StopwordTypeThree
from .stopword_type_two import StopwordTypeTwo
from .stopword_type_zero import StopwordTypeZero

StopwordType = typing.Union[
    StopwordTypeZero, StopwordTypeOne, StopwordTypeTwo, StopwordTypeThree, StopwordTypeFour, StopwordTypeCustom
]

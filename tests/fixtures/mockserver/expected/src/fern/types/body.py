

from __future__ import annotations

import typing

from .body_eleven import BodyEleven
from .body_fields import BodyFields
from .body_fifteen import BodyFifteen
from .body_five import BodyFive
from .body_four import BodyFour
from .body_fourteen import BodyFourteen
from .body_method import BodyMethod
from .body_nine import BodyNine
from .body_nineteen import BodyNineteen
from .body_one import BodyOne
from .body_operation_name import BodyOperationName
from .body_seven import BodySeven
from .body_seventeen import BodySeventeen
from .body_six import BodySix
from .body_sixteen import BodySixteen
from .body_ten import BodyTen
from .body_thirteen import BodyThirteen
from .body_three import BodyThree
from .body_twenty import BodyTwenty
from .body_twenty_one import BodyTwentyOne
from .body_twenty_three import BodyTwentyThree
from .body_twenty_two import BodyTwentyTwo
from .body_zero import BodyZero

if typing.TYPE_CHECKING:
    from .body_body_all_of import BodyBodyAllOf
Body = typing.Union[
    BodyZero,
    BodyOne,
    typing.Dict[str, typing.Any],
    BodyThree,
    BodyFour,
    BodyFive,
    BodySix,
    BodySeven,
    str,
    BodyNine,
    BodyTen,
    BodyEleven,
    "BodyBodyAllOf",
    BodyThirteen,
    BodyFourteen,
    BodyFifteen,
    BodySixteen,
    BodySeventeen,
    BodyFields,
    BodyNineteen,
    BodyTwenty,
    BodyTwentyOne,
    BodyTwentyTwo,
    BodyTwentyThree,
    BodyMethod,
    BodyOperationName,
]

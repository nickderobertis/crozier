

import typing

from .val_author_type_one import ValAuthorTypeOne
from .val_author_type_zero import ValAuthorTypeZero

ValAuthorType = typing.Union[ValAuthorTypeZero, ValAuthorTypeOne]

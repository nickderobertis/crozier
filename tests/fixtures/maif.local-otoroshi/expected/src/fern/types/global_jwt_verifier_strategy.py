

import typing

from .pass_through import PassThrough
from .sign import Sign
from .transform import Transform

GlobalJwtVerifierStrategy = typing.Union[PassThrough, Sign, Transform]

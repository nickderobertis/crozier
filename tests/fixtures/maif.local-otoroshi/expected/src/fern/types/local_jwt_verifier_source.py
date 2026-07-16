

import typing

from .in_cookie import InCookie
from .in_header import InHeader
from .in_query_param import InQueryParam

LocalJwtVerifierSource = typing.Union[InQueryParam, InHeader, InCookie]



import typing

from .in_cookie import InCookie
from .in_header import InHeader
from .in_query_param import InQueryParam

TransformSettingsLocation = typing.Union[InQueryParam, InHeader, InCookie]



import typing

from .geo_target import GeoTarget
from .proxy_location import ProxyLocation

CreateBrowserProfileRequestProxyLocation = typing.Union[ProxyLocation, GeoTarget, typing.Dict[str, typing.Any]]

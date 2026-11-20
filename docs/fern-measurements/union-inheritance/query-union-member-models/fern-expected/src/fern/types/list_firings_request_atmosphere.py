

import typing

from .list_firings_request_atmosphere_one_item import ListFiringsRequestAtmosphereOneItem
from .list_firings_request_atmosphere_zero import ListFiringsRequestAtmosphereZero

ListFiringsRequestAtmosphere = typing.Union[
    typing.Optional[ListFiringsRequestAtmosphereZero], typing.List[typing.Optional[ListFiringsRequestAtmosphereOneItem]]
]

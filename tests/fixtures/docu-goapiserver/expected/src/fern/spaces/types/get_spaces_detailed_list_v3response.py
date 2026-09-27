

import typing

from ...types.spaces_aggregate import SpacesAggregate
from ...types.spaces_periods import SpacesPeriods
from ...types.spaces_projection import SpacesProjection
from ...types.spaces_row import SpacesRow

GetSpacesDetailedListV3Response = typing.Union[
    typing.List[SpacesRow], typing.List[SpacesAggregate], typing.List[SpacesProjection], typing.List[SpacesPeriods]
]

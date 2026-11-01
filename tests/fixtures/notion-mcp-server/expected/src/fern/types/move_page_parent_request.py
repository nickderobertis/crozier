

import typing

from .move_page_parent_request_database_id import MovePageParentRequestDatabaseId
from .move_page_parent_request_page_id import MovePageParentRequestPageId
from .move_page_parent_request_type import MovePageParentRequestType

MovePageParentRequest = typing.Union[
    MovePageParentRequestPageId, MovePageParentRequestDatabaseId, MovePageParentRequestType
]

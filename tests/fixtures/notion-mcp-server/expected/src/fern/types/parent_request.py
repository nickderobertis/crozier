

import typing

from .data_source_id_parent_request import DataSourceIdParentRequest
from .page_id_parent_request import PageIdParentRequest
from .parent_request_type import ParentRequestType

ParentRequest = typing.Union[PageIdParentRequest, DataSourceIdParentRequest, ParentRequestType]

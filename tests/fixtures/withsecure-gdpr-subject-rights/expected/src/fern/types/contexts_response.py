

import typing

from .contexts_response_item import ContextsResponseItem

ContextsResponse = typing.List[ContextsResponseItem]
"""
This is a list of personal data contexts, together with required authentication identifiers needed for the export and delete operations.
"""

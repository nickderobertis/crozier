

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notebooks_list_response_notebooks_item import NotebooksListResponseNotebooksItem


class NotebooksListResponse(UniversalBaseModel):
    notebooks: typing.List[NotebooksListResponseNotebooksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

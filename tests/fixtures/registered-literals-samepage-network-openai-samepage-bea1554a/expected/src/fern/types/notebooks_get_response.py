

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notebooks_get_response_notebooks_item import NotebooksGetResponseNotebooksItem


class NotebooksGetResponse(UniversalBaseModel):
    notebooks: typing.List[NotebooksGetResponseNotebooksItem] = pydantic.Field()
    """
    Notebooks this account has access to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

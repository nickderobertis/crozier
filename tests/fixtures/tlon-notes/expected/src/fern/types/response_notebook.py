

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notebook_summary import NotebookSummary


class ResponseNotebook(UniversalBaseModel):
    """
    Returned by `create-notebook` — the new notebook's summary so
    the caller learns the slugified flag + metadata without a
    follow-up read.
    """

    notebook: NotebookSummary

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

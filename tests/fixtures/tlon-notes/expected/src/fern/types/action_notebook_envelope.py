

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .a_notebook import ANotebook


class ActionNotebookEnvelope(UniversalBaseModel):
    flag: str = pydantic.Field()
    """
    Notebook flag as a `~ship/name` string (e.g. `~zod/my-notebook`). Note this envelope takes the string form, unlike the `{host, flagName}` object used by create-group-notebook.
    """

    action: ANotebook

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ActionNotebookEnvelope)

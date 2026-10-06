

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_changes_item import TransactionChangesItem
from .transaction_source import TransactionSource


class Transaction(UniversalBaseModel):
    """
    An atomic batch of changes applied to a NotebookDocument.

        `source` identifies the writer (e.g. `"frontend"`, `"kernel"`).
        `version` is `None` when created and stamped by
        `NotebookDocument.apply()`.
    """

    changes: typing.List[TransactionChangesItem]
    source: TransactionSource
    version: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

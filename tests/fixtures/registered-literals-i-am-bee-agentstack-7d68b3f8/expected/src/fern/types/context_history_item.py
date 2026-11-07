

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_history_item_data_output import ContextHistoryItemDataOutput
from .context_history_item_kind import ContextHistoryItemKind


class ContextHistoryItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    data: ContextHistoryItemDataOutput
    created_at: typing.Optional[dt.datetime] = None
    context_id: str
    kind: typing.Optional[ContextHistoryItemKind] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_action_history_page_actions_item import AccountActionHistoryPageActionsItem


class AccountActionHistoryPage(UniversalBaseModel):
    actions: typing.List[AccountActionHistoryPageActionsItem]
    next_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextCursor"), pydantic.Field(alias="nextCursor")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

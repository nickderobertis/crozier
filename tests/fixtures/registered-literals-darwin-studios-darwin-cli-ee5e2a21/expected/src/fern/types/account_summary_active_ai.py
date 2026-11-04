

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_summary_active_ai_role import AccountSummaryActiveAiRole
from .account_summary_active_ai_source import AccountSummaryActiveAiSource


class AccountSummaryActiveAi(UniversalBaseModel):
    ai_id: typing_extensions.Annotated[str, FieldMetadata(alias="aiId"), pydantic.Field(alias="aiId")]
    type: str
    name: str
    role: AccountSummaryActiveAiRole
    source: AccountSummaryActiveAiSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

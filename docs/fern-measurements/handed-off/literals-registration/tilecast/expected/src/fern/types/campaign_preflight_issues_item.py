

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_preflight_issues_item_severity import CampaignPreflightIssuesItemSeverity


class CampaignPreflightIssuesItem(UniversalBaseModel):
    severity: CampaignPreflightIssuesItemSeverity
    code: str
    message: str
    block_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blockId"), pydantic.Field(alias="blockId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_destination import CampaignDestination
from .campaign_snapshot import CampaignSnapshot


class Campaign(UniversalBaseModel):
    id: str
    name: str
    description: str
    owner_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")
    ] = None
    timezone: str
    campaign_start: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="campaignStart"), pydantic.Field(alias="campaignStart")
    ] = None
    campaign_end: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="campaignEnd"), pydantic.Field(alias="campaignEnd")
    ] = None
    destinations: typing.List[CampaignDestination]
    draft: CampaignSnapshot
    draft_revision: typing_extensions.Annotated[
        int, FieldMetadata(alias="draftRevision"), pydantic.Field(alias="draftRevision")
    ]
    status: str
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

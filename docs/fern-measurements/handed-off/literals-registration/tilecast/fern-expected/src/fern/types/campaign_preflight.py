

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .campaign_preflight_issues_item import CampaignPreflightIssuesItem


class CampaignPreflight(UniversalBaseModel):
    valid: bool
    issues: typing.List[CampaignPreflightIssuesItem]
    block_count: typing_extensions.Annotated[int, FieldMetadata(alias="blockCount"), pydantic.Field(alias="blockCount")]
    destination_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="destinationCount"), pydantic.Field(alias="destinationCount")
    ]
    screen_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="screenCount"), pydantic.Field(alias="screenCount")
    ]
    location_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="locationCount"), pydantic.Field(alias="locationCount")
    ]
    previewed_screen_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="previewedScreenCount"), pydantic.Field(alias="previewedScreenCount")
    ]
    preview_screen_limit: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="previewScreenLimit"),
        pydantic.Field(
            alias="previewScreenLimit",
            description="Maximum number of target screens used for scheduler-overlap previews.",
        ),
    ]
    """
    Maximum number of target screens used for scheduler-overlap previews.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

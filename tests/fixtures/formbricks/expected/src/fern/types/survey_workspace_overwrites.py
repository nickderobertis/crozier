

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_workspace_overwrites_overlay import SurveyWorkspaceOverwritesOverlay
from .survey_workspace_overwrites_placement import SurveyWorkspaceOverwritesPlacement


class SurveyWorkspaceOverwrites(UniversalBaseModel):
    """
    Workspace-specific overwrites
    """

    brand_color: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="brandColor"), pydantic.Field(alias="brandColor")
    ] = None
    highlight_border_color: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="highlightBorderColor"), pydantic.Field(alias="highlightBorderColor")
    ] = None
    placement: typing.Optional[SurveyWorkspaceOverwritesPlacement] = None
    click_outside_close: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="clickOutsideClose"), pydantic.Field(alias="clickOutsideClose")
    ] = None
    overlay: typing.Optional[SurveyWorkspaceOverwritesOverlay] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

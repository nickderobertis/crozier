

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1create_project_body_region_selection_smart_group_code import V1CreateProjectBodyRegionSelectionSmartGroupCode
from .v1create_project_body_region_selection_specific_code import V1CreateProjectBodyRegionSelectionSpecificCode


class V1CreateProjectBodyRegionSelection_Specific(UniversalBaseModel):
    """
    Region selection. Only one of region or region_selection can be specified.
    """

    type: typing.Literal["specific"] = "specific"
    code: V1CreateProjectBodyRegionSelectionSpecificCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class V1CreateProjectBodyRegionSelection_SmartGroup(UniversalBaseModel):
    """
    Region selection. Only one of region or region_selection can be specified.
    """

    type: typing.Literal["smartGroup"] = "smartGroup"
    code: V1CreateProjectBodyRegionSelectionSmartGroupCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


V1CreateProjectBodyRegionSelection = typing_extensions.Annotated[
    typing.Union[V1CreateProjectBodyRegionSelection_Specific, V1CreateProjectBodyRegionSelection_SmartGroup],
    pydantic.Field(discriminator="type"),
]

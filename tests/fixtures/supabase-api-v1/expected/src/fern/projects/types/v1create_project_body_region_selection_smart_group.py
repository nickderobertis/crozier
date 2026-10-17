

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1create_project_body_region_selection_smart_group_code import V1CreateProjectBodyRegionSelectionSmartGroupCode


class V1CreateProjectBodyRegionSelectionSmartGroup(UniversalBaseModel):
    code: V1CreateProjectBodyRegionSelectionSmartGroupCode = pydantic.Field()
    """
    The Smart Region Group's code. The codes supported are not a stable API, and should be retrieved from the /available-regions endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

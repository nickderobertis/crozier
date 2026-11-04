

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightsListProjectBranchesResponse(UniversalBaseModel):
    """
    Project branches response.
    """

    org_id: typing.Any
    project_id: typing.Any
    branches: typing.List[str] = pydantic.Field()
    """
    A list of all the branches for a given project.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

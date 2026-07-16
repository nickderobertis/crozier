

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchTeamMembersFilter(UniversalBaseModel):
    """
    Represents a filter used in a search for `TeamMember` objects. `AND` logic is applied
    between the individual fields, and `OR` logic is applied within list-based fields.
    For example, setting this filter value:
    ```
    filter = (locations_ids = ["A", "B"], status = ACTIVE)
    ```
    returns only active team members assigned to either location "A" or "B".
    """

    location_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    When present, filters by team members assigned to the specified locations.
    When empty, includes team members assigned to any location.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    When present, filters by team members who match the given status.
    When empty, includes team members of all statuses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

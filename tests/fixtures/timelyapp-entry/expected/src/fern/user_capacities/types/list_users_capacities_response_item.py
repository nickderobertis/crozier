

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.v1user_capacity import V1UserCapacity


class ListUsersCapacitiesResponseItem(UniversalBaseModel):
    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    User ID
    """

    capacities: typing.Optional[typing.List[V1UserCapacity]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

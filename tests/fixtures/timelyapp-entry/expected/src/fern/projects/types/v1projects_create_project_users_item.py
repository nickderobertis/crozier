

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ProjectsCreateProjectUsersItem(UniversalBaseModel):
    user_id: int = pydantic.Field()
    """
    User ID to assign to the project
    """

    hour_rate: float = pydantic.Field()
    """
    Hourly rate for this user on the project
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

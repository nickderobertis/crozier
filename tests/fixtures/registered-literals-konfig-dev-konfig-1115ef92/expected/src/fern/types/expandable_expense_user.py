

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExpandableExpenseUser(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique ID for the User.
    """

    first_name: str = pydantic.Field()
    """
    First name of the User.
    """

    last_name: str = pydantic.Field()
    """
    Last name of the User.
    """

    department_id: typing.Optional[str] = None
    location_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

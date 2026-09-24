

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1UserRole(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Describes user role like **admin**, **manager**, **employee** or **team_lead**
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

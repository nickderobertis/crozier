

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrganizationCreate(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the organization.
    """

    privileged_tools: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the organization has access to privileged tools.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

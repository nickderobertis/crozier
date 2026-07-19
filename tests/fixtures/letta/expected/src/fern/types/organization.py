

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Organization(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Org
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the organization.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The creation date of the organization.
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

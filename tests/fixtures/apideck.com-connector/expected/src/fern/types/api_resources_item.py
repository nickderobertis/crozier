

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_status import ResourceStatus


class ApiResourcesItem(UniversalBaseModel):
    excluded_from_coverage: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Exclude from mapping coverage
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the resource, typically a lowercased version of its name.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the resource (plural)
    """

    status: typing.Optional[ResourceStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

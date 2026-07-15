

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resource_id import ResourceId
from .resource_status import ResourceStatus


class LinkedConnectorResource(UniversalBaseModel):
    downstream_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the resource in the Connector's API (downstream)
    """

    downstream_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the resource in the Connector's API (downstream)
    """

    id: typing.Optional[ResourceId] = None
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

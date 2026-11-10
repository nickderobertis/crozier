

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connected_application import ConnectedApplication
from .request_id import RequestId


class ItemApplicationListResponse(UniversalBaseModel):
    """
    Describes the connected application for a particular end user.
    """

    applications: typing.List[ConnectedApplication] = pydantic.Field()
    """
    A list of connected applications.
    """

    request_id: typing.Optional[RequestId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

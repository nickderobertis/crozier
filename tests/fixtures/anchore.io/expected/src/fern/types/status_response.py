

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StatusResponse(UniversalBaseModel):
    """
    System status response
    """

    available: typing.Optional[bool] = None
    busy: typing.Optional[bool] = None
    db_version: typing.Optional[str] = None
    detail: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    message: typing.Optional[str] = None
    up: typing.Optional[bool] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

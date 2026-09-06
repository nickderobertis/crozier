

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApplicationUserRoleConnectionResponse(UniversalBaseModel):
    platform_name: typing.Optional[str] = None
    platform_username: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

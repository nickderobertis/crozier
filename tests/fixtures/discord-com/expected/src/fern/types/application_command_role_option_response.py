

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ApplicationCommandRoleOptionResponse(UniversalBaseModel):
    type: int
    name: str
    name_localized: typing.Optional[str] = None
    name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    description: str
    description_localized: typing.Optional[str] = None
    description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

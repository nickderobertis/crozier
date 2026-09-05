

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .function_group_access_rights_get import FunctionGroupAccessRightsGet


class EnvelopeDictNewTypeFunctionGroupAccessRightsGet(UniversalBaseModel):
    data: typing.Optional[typing.Dict[str, typing.Optional[FunctionGroupAccessRightsGet]]] = None
    error: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

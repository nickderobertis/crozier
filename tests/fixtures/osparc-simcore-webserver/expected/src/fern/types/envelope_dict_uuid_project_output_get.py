

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_output_get import ProjectOutputGet


class EnvelopeDictUuidProjectOutputGet(UniversalBaseModel):
    data: typing.Optional[typing.Dict[str, typing.Optional[ProjectOutputGet]]] = None
    error: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

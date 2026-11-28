

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_form_definition_version import BaseFormDefinitionVersion


class FormDefinitionVersion(BaseFormDefinitionVersion):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    API ID of this version
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

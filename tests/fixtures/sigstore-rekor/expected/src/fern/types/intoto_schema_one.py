

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .intoto_schema_one_content import IntotoSchemaOneContent


class IntotoSchemaOne(UniversalBaseModel):
    """
    Schema for intoto object
    """

    content: IntotoSchemaOneContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

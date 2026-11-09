

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PublishPolicy(UniversalBaseModel):
    errors: typing.List[typing.Dict[str, typing.Any]]
    is_valid: typing_extensions.Annotated[bool, FieldMetadata(alias="isValid"), pydantic.Field(alias="isValid")]
    policies: typing.List[typing.Dict[str, typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

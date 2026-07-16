

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetUserExternalIdResponseUserUserFields(UniversalBaseModel):
    f_1: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="1"), pydantic.Field(alias="1")] = None
    f_2: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="2"), pydantic.Field(alias="2")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

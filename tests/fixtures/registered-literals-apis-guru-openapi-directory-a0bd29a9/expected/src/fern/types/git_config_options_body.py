

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GitConfigOptionsBody(UniversalBaseModel):
    user_email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userEmail"), pydantic.Field(alias="userEmail")
    ] = None
    user_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userName"), pydantic.Field(alias="userName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

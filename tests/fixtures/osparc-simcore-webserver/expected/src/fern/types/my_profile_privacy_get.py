

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MyProfilePrivacyGet(UniversalBaseModel):
    hide_username: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hideUsername"), pydantic.Field(alias="hideUsername")
    ]
    hide_fullname: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hideFullname"), pydantic.Field(alias="hideFullname")
    ]
    hide_email: typing_extensions.Annotated[bool, FieldMetadata(alias="hideEmail"), pydantic.Field(alias="hideEmail")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

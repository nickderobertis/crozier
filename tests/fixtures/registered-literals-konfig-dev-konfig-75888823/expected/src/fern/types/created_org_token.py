

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .org_token import OrgToken


class CreatedOrgToken(UniversalBaseModel):
    plain_text_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="plainTextToken"), pydantic.Field(alias="plainTextToken")
    ]
    org_token: typing_extensions.Annotated[OrgToken, FieldMetadata(alias="orgToken"), pydantic.Field(alias="orgToken")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

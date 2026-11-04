

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganizationUserInvitation(UniversalBaseModel):
    email: typing.Optional[str] = None
    roles: typing.List[str]
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

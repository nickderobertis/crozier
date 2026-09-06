

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .contact_role_enum import ContactRoleEnum
from .status_enum import StatusEnum
from .system_enum import SystemEnum


class AuthorisationDomainUserUpdateRequest(UniversalBaseModel):
    contact_role: typing_extensions.Annotated[
        typing.Optional[ContactRoleEnum], FieldMetadata(alias="ContactRole"), pydantic.Field(alias="ContactRole")
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    system: typing_extensions.Annotated[
        typing.Optional[SystemEnum], FieldMetadata(alias="System"), pydantic.Field(alias="System")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

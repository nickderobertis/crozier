

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_head200response_permissions_opened_as import DocHead200ResponsePermissionsOpenedAs


class DocHead200ResponsePermissions(UniversalBaseModel):
    known: bool
    bits: typing.Optional[int] = None
    all_allowed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allAllowed"), pydantic.Field(alias="allAllowed")
    ] = None
    opened_as: typing_extensions.Annotated[
        typing.Optional[DocHead200ResponsePermissionsOpenedAs],
        FieldMetadata(alias="openedAs"),
        pydantic.Field(alias="openedAs"),
    ] = None
    security_handler_revision: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="securityHandlerRevision"),
        pydantic.Field(alias="securityHandlerRevision"),
    ] = None
    can_upgrade_to_owner: typing_extensions.Annotated[
        bool, FieldMetadata(alias="canUpgradeToOwner"), pydantic.Field(alias="canUpgradeToOwner")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

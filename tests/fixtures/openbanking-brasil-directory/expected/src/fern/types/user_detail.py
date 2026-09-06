

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .org_access_detail import OrgAccessDetail
from .terms_and_conditions_details import TermsAndConditionsDetails
from .user_detail_basic_information import UserDetailBasicInformation


class UserDetail(UniversalBaseModel):
    basic_information: typing_extensions.Annotated[
        typing.Optional[UserDetailBasicInformation],
        FieldMetadata(alias="BasicInformation"),
        pydantic.Field(alias="BasicInformation"),
    ] = None
    certification_manager: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="CertificationManager"),
        pydantic.Field(alias="CertificationManager", description="Is the user a certification manager"),
    ] = None
    """
    Is the user a certification manager
    """

    directory_terms_and_conditions_details: typing_extensions.Annotated[
        typing.Optional[TermsAndConditionsDetails],
        FieldMetadata(alias="DirectoryTermsAndConditionsDetails"),
        pydantic.Field(alias="DirectoryTermsAndConditionsDetails"),
    ] = None
    org_access_details: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, OrgAccessDetail]],
        FieldMetadata(alias="OrgAccessDetails"),
        pydantic.Field(
            alias="OrgAccessDetails",
            description="Map Key - OrgId, Map Value - Org Access Detail(containing info about org admin and domain role)",
        ),
    ] = None
    """
    Map Key - OrgId, Map Value - Org Access Detail(containing info about org admin and domain role)
    """

    super_user: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="SuperUser"),
        pydantic.Field(alias="SuperUser", description="Is the user a super user"),
    ] = None
    """
    Is the user a super user
    """

    system_user: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="SystemUser"),
        pydantic.Field(alias="SystemUser", description="Is the user a system user"),
    ] = None
    """
    Is the user a system user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

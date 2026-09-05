

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author import Author
from .lower_case_email_str import LowerCaseEmailStr
from .service_group_access_rights_v2 import ServiceGroupAccessRightsV2
from .service_release import ServiceRelease
from .service_type import ServiceType


class CatalogServiceGet(UniversalBaseModel):
    key: str
    version: str
    name: str
    description: str
    version_display: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="versionDisplay"), pydantic.Field(alias="versionDisplay")
    ] = None
    contact: typing.Optional[LowerCaseEmailStr] = None
    type: ServiceType
    thumbnail: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    description_ui: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="descriptionUi"), pydantic.Field(alias="descriptionUi")
    ] = None
    authors: typing.List[Author]
    owner: typing.Optional[LowerCaseEmailStr] = pydantic.Field(default=None)
    """
    None when the owner email cannot be found in the database
    """

    inputs: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    inputs with extended information
    """

    outputs: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    outputs with extended information
    """

    boot_options: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="bootOptions"),
        pydantic.Field(alias="bootOptions"),
    ] = None
    min_visible_inputs: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="minVisibleInputs"), pydantic.Field(alias="minVisibleInputs")
    ] = None
    access_rights: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]],
        FieldMetadata(alias="accessRights"),
        pydantic.Field(alias="accessRights"),
    ] = None
    classifiers: typing.Optional[typing.List[str]] = None
    quality: typing.Optional[typing.Dict[str, typing.Any]] = None
    release_notes_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="releaseNotesUrl"), pydantic.Field(alias="releaseNotesUrl")
    ] = None
    history: typing.Optional[typing.List[ServiceRelease]] = pydantic.Field(default=None)
    """
    history of releases for this service at this point in time, starting from the newest to the oldest. It includes current release.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

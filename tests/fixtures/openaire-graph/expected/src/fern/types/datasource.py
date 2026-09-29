

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .container import Container
from .datasource_pid import DatasourcePid
from .datasource_scheme_value import DatasourceSchemeValue


class Datasource(UniversalBaseModel):
    id: typing.Optional[str] = None
    original_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="originalIds"), pydantic.Field(alias="originalIds")
    ] = None
    pids: typing.Optional[typing.List[DatasourcePid]] = None
    type: typing.Optional[DatasourceSchemeValue] = None
    openaire_compatibility: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="openaireCompatibility"),
        pydantic.Field(alias="openaireCompatibility"),
    ] = None
    official_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="officialName"), pydantic.Field(alias="officialName")
    ] = None
    english_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="englishName"), pydantic.Field(alias="englishName")
    ] = None
    website_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="websiteUrl"), pydantic.Field(alias="websiteUrl")
    ] = None
    logo_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logoUrl"), pydantic.Field(alias="logoUrl")
    ] = None
    date_of_validation: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dateOfValidation"), pydantic.Field(alias="dateOfValidation")
    ] = None
    description: typing.Optional[str] = None
    subjects: typing.Optional[typing.List[str]] = None
    languages: typing.Optional[typing.List[str]] = None
    content_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="contentTypes"), pydantic.Field(alias="contentTypes")
    ] = None
    release_start_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="releaseStartDate"), pydantic.Field(alias="releaseStartDate")
    ] = None
    release_end_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="releaseEndDate"), pydantic.Field(alias="releaseEndDate")
    ] = None
    mission_statement_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="missionStatementUrl"), pydantic.Field(alias="missionStatementUrl")
    ] = None
    access_rights: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accessRights"), pydantic.Field(alias="accessRights")
    ] = None
    upload_rights: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uploadRights"), pydantic.Field(alias="uploadRights")
    ] = None
    database_access_restriction: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="databaseAccessRestriction"),
        pydantic.Field(alias="databaseAccessRestriction"),
    ] = None
    data_upload_restriction: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dataUploadRestriction"),
        pydantic.Field(alias="dataUploadRestriction"),
    ] = None
    versioning: typing.Optional[bool] = None
    citation_guideline_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="citationGuidelineUrl"), pydantic.Field(alias="citationGuidelineUrl")
    ] = None
    pid_systems: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pidSystems"), pydantic.Field(alias="pidSystems")
    ] = None
    certificates: typing.Optional[str] = None
    policies: typing.Optional[typing.List[str]] = None
    journal: typing.Optional[Container] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

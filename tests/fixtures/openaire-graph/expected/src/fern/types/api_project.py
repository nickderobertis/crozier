

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .funder import Funder
from .granted import Granted
from .programme import Programme


class ApiProject(UniversalBaseModel):
    id: typing.Optional[str] = None
    code: typing.Optional[str] = None
    acronym: typing.Optional[str] = None
    title: typing.Optional[str] = None
    website_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="websiteUrl"), pydantic.Field(alias="websiteUrl")
    ] = None
    start_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")
    ] = None
    end_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")
    ] = None
    call_identifier: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="callIdentifier"), pydantic.Field(alias="callIdentifier")
    ] = None
    keywords: typing.Optional[str] = None
    open_access_mandate_for_publications: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="openAccessMandateForPublications"),
        pydantic.Field(alias="openAccessMandateForPublications"),
    ] = None
    open_access_mandate_for_dataset: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="openAccessMandateForDataset"),
        pydantic.Field(alias="openAccessMandateForDataset"),
    ] = None
    subjects: typing.Optional[typing.List[str]] = None
    fundings: typing.Optional[typing.List[Funder]] = None
    summary: typing.Optional[str] = None
    granted: typing.Optional[Granted] = None
    h2020programmes: typing_extensions.Annotated[
        typing.Optional[typing.List[Programme]],
        FieldMetadata(alias="h2020Programmes"),
        pydantic.Field(alias="h2020Programmes"),
    ] = None
    original_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="originalIds"), pydantic.Field(alias="originalIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

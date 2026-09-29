

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author import Author
from .best_access_right import BestAccessRight
from .container import Container
from .geo_location import GeoLocation
from .graph_result_open_access_color import GraphResultOpenAccessColor
from .indicator import Indicator
from .instance import Instance
from .language import Language
from .result_country import ResultCountry
from .result_pid import ResultPid
from .subject import Subject


class GraphResult(UniversalBaseModel):
    authors: typing.Optional[typing.List[Author]] = None
    open_access_color: typing_extensions.Annotated[
        typing.Optional[GraphResultOpenAccessColor],
        FieldMetadata(alias="openAccessColor"),
        pydantic.Field(alias="openAccessColor"),
    ] = None
    publicly_funded: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="publiclyFunded"), pydantic.Field(alias="publiclyFunded")
    ] = None
    type: typing.Optional[str] = None
    language: typing.Optional[Language] = None
    countries: typing.Optional[typing.List[ResultCountry]] = None
    subjects: typing.Optional[typing.List[Subject]] = None
    main_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mainTitle"), pydantic.Field(alias="mainTitle")
    ] = None
    sub_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="subTitle"), pydantic.Field(alias="subTitle")
    ] = None
    descriptions: typing.Optional[typing.List[str]] = None
    publication_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publicationDate"), pydantic.Field(alias="publicationDate")
    ] = None
    publisher: typing.Optional[str] = None
    embargo_end_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="embargoEndDate"), pydantic.Field(alias="embargoEndDate")
    ] = None
    sources: typing.Optional[typing.List[str]] = None
    formats: typing.Optional[typing.List[str]] = None
    contributors: typing.Optional[typing.List[str]] = None
    coverages: typing.Optional[typing.List[str]] = None
    best_access_right: typing_extensions.Annotated[
        typing.Optional[BestAccessRight],
        FieldMetadata(alias="bestAccessRight"),
        pydantic.Field(alias="bestAccessRight"),
    ] = None
    container: typing.Optional[Container] = None
    documentation_urls: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="documentationUrls"),
        pydantic.Field(alias="documentationUrls"),
    ] = None
    code_repository_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="codeRepositoryUrl"), pydantic.Field(alias="codeRepositoryUrl")
    ] = None
    programming_language: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="programmingLanguage"), pydantic.Field(alias="programmingLanguage")
    ] = None
    contact_people: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="contactPeople"), pydantic.Field(alias="contactPeople")
    ] = None
    contact_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="contactGroups"), pydantic.Field(alias="contactGroups")
    ] = None
    tools: typing.Optional[typing.List[str]] = None
    size: typing.Optional[str] = None
    version: typing.Optional[str] = None
    geo_locations: typing_extensions.Annotated[
        typing.Optional[typing.List[GeoLocation]],
        FieldMetadata(alias="geoLocations"),
        pydantic.Field(alias="geoLocations"),
    ] = None
    id: typing.Optional[str] = None
    original_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="originalIds"), pydantic.Field(alias="originalIds")
    ] = None
    pids: typing.Optional[typing.List[ResultPid]] = None
    date_of_collection: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dateOfCollection"), pydantic.Field(alias="dateOfCollection")
    ] = None
    last_update_time_stamp: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lastUpdateTimeStamp"), pydantic.Field(alias="lastUpdateTimeStamp")
    ] = None
    indicators: typing.Optional[Indicator] = None
    instances: typing.Optional[typing.List[Instance]] = None
    is_green: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isGreen"), pydantic.Field(alias="isGreen")
    ] = None
    is_in_diamond_journal: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isInDiamondJournal"), pydantic.Field(alias="isInDiamondJournal")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

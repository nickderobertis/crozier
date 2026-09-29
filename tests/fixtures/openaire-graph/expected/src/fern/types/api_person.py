

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .context import Context
from .measure import Measure
from .person_topic import PersonTopic


class ApiPerson(UniversalBaseModel):
    id: typing.Optional[str] = None
    original_id: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="originalId"), pydantic.Field(alias="originalId")
    ] = None
    given_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="givenName"), pydantic.Field(alias="givenName")
    ] = None
    family_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="familyName"), pydantic.Field(alias="familyName")
    ] = None
    alternative_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="alternativeNames"),
        pydantic.Field(alias="alternativeNames"),
    ] = None
    biography: typing.Optional[str] = None
    subject: typing.Optional[typing.List[PersonTopic]] = None
    indicator: typing.Optional[typing.List[Measure]] = None
    context: typing.Optional[typing.List[Context]] = None
    consent: typing.Optional[bool] = None
    co_authors: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="coAuthors"), pydantic.Field(alias="coAuthors")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

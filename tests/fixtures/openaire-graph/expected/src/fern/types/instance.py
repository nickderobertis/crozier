

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_right import AccessRight
from .alternate_identifier import AlternateIdentifier
from .apc import Apc
from .result_pid import ResultPid


class Instance(UniversalBaseModel):
    pids: typing.Optional[typing.List[ResultPid]] = None
    alternate_identifiers: typing_extensions.Annotated[
        typing.Optional[typing.List[AlternateIdentifier]],
        FieldMetadata(alias="alternateIdentifiers"),
        pydantic.Field(alias="alternateIdentifiers"),
    ] = None
    license: typing.Optional[str] = None
    access_right: typing_extensions.Annotated[
        typing.Optional[AccessRight], FieldMetadata(alias="accessRight"), pydantic.Field(alias="accessRight")
    ] = None
    type: typing.Optional[str] = None
    urls: typing.Optional[typing.List[str]] = None
    article_processing_charge: typing_extensions.Annotated[
        typing.Optional[Apc],
        FieldMetadata(alias="articleProcessingCharge"),
        pydantic.Field(alias="articleProcessingCharge"),
    ] = None
    publication_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publicationDate"), pydantic.Field(alias="publicationDate")
    ] = None
    refereed: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

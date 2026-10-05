

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntryNode(UniversalBaseModel):
    id: str
    preceding_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="precedingLines"), pydantic.Field(alias="precedingLines")
    ] = None
    main_language: typing_extensions.Annotated[
        str, FieldMetadata(alias="mainLanguage"), pydantic.Field(alias="mainLanguage")
    ]
    tags: typing.Dict[str, typing.List[str]]
    tags_ids: typing_extensions.Annotated[
        typing.Dict[str, typing.List[str]], FieldMetadata(alias="tagsIds"), pydantic.Field(alias="tagsIds")
    ]
    properties: typing.Dict[str, str]
    comments: typing.Dict[str, typing.List[str]]
    is_external: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isExternal"), pydantic.Field(alias="isExternal")
    ] = None
    original_taxonomy: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="originalTaxonomy"), pydantic.Field(alias="originalTaxonomy")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

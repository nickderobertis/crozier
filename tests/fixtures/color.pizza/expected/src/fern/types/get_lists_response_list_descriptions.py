

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_description import ListDescription


class GetListsResponseListDescriptions(UniversalBaseModel):
    basic: typing.Optional[ListDescription] = None
    best_of: typing_extensions.Annotated[
        typing.Optional[ListDescription], FieldMetadata(alias="bestOf"), pydantic.Field(alias="bestOf")
    ] = None
    chinese_traditional: typing_extensions.Annotated[
        typing.Optional[ListDescription],
        FieldMetadata(alias="chineseTraditional"),
        pydantic.Field(alias="chineseTraditional"),
    ] = None
    default: typing.Optional[ListDescription] = None
    french: typing.Optional[ListDescription] = None
    html: typing.Optional[ListDescription] = None
    japanese_traditional: typing_extensions.Annotated[
        typing.Optional[ListDescription],
        FieldMetadata(alias="japaneseTraditional"),
        pydantic.Field(alias="japaneseTraditional"),
    ] = None
    le_corbusier: typing_extensions.Annotated[
        typing.Optional[ListDescription], FieldMetadata(alias="leCorbusier"), pydantic.Field(alias="leCorbusier")
    ] = None
    nbs_iscc: typing_extensions.Annotated[
        typing.Optional[ListDescription], FieldMetadata(alias="nbsIscc"), pydantic.Field(alias="nbsIscc")
    ] = None
    ntc: typing.Optional[ListDescription] = None
    osxcrayons: typing.Optional[ListDescription] = None
    ral: typing.Optional[ListDescription] = None
    ridgway: typing.Optional[ListDescription] = None
    risograph: typing.Optional[ListDescription] = None
    sanzo_wada_i: typing_extensions.Annotated[
        typing.Optional[ListDescription], FieldMetadata(alias="sanzoWadaI"), pydantic.Field(alias="sanzoWadaI")
    ] = None
    thesaurus: typing.Optional[ListDescription] = None
    werner: typing.Optional[ListDescription] = None
    wikipedia: typing.Optional[ListDescription] = None
    windows: typing.Optional[ListDescription] = None
    x11: typing.Optional[ListDescription] = None
    xkcd: typing.Optional[ListDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field_type import FieldType


class SchemaField(UniversalBaseModel):
    """
    Defines a field in index schema: field, stored, indexed , field_type, facet, boost.
    """

    field: str = pydantic.Field()
    """
    unique name of a field
    """

    store: bool = pydantic.Field()
    """
    only stored fields are returned in the search results
    """

    index_lexical: bool = pydantic.Field()
    """
    only indexed fields can be searched
    """

    index_vector: typing.Optional[bool] = pydantic.Field(default=None)
    """
    only indexed fields can be searched
    """

    field_type: FieldType = pydantic.Field()
    """
    type of a field
    """

    facet: typing.Optional[bool] = pydantic.Field(default=None)
    """
    optional faceting for a field
    Faceting can be enabled both for string field type and numerical field types.
    both numerical and string fields can be indexed (indexed=true) and stored (stored=true) in the json document,
    but with field_facet=true they are additionally stored in a binary format, for fast faceting and sorting without docstore access (decompression, deserialization)
    """

    longest: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicate the longest field in schema.
    Otherwise the longest field will be automatically detected in first index_document.
    Setting/detecting the longest field ensures efficient index encoding.
    """

    boost: typing.Optional[float] = pydantic.Field(default=None)
    """
    optional custom weight factor for Bm25 ranking
    """

    dictionary_source: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if both indexed=true and dictionary_source=true then the terms from this field are added to dictionary to the spelling correction dictionary.
    if disabled, then a manually generated dictionary can be used: {index_path}/dictionary.csv
    """

    completion_source: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if both indexed=true and completion_source=true then the n-grams (unigrams, bigrams, trigrams) from this field are added to the auto-completion list.
    if disabled, then a manually generated completion list can be used: {index_path}/completions.csv
    it is recommended to enable completion_source only for fields that contain short text with high-quality terms for auto-completion, e.g. title, author, category, product name, tags,
    in order to keep the extraction time and RAM requirement for completions low and the completions relevance high.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

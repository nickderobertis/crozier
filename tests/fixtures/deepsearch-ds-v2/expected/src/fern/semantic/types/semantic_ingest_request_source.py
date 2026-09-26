

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SemanticIngestRequestSource_Url(UniversalBaseModel):
    type: typing.Literal["url"] = "url"
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SemanticIngestRequestSource_PublicDataDocument(UniversalBaseModel):
    type: typing.Literal["public_data_document"] = "public_data_document"
    elastic_id: str
    index_key: str
    document_hash: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SemanticIngestRequestSource_PrivateDataDocument(UniversalBaseModel):
    type: typing.Literal["private_data_document"] = "private_data_document"
    proj_key: str
    index_key: str
    document_hash: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SemanticIngestRequestSource_PrivateDataCollection(UniversalBaseModel):
    type: typing.Literal["private_data_collection"] = "private_data_collection"
    proj_key: str
    index_key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SemanticIngestRequestSource = typing_extensions.Annotated[
    typing.Union[
        SemanticIngestRequestSource_Url,
        SemanticIngestRequestSource_PublicDataDocument,
        SemanticIngestRequestSource_PrivateDataDocument,
        SemanticIngestRequestSource_PrivateDataCollection,
    ],
    pydantic.Field(discriminator="type"),
]

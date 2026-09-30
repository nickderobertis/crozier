

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .solr_response_response import SolrResponseResponse
from .solr_response_response_header import SolrResponseResponseHeader


class SolrResponse(UniversalBaseModel):
    response: typing.Optional[SolrResponseResponse] = None
    response_header: typing_extensions.Annotated[
        typing.Optional[SolrResponseResponseHeader],
        FieldMetadata(alias="responseHeader"),
        pydantic.Field(alias="responseHeader"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

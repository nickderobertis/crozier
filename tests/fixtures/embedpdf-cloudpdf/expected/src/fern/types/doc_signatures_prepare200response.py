

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_prepare200response_algorithm import DocSignaturesPrepare200ResponseAlgorithm
from .doc_signatures_prepare200response_expected_version import DocSignaturesPrepare200ResponseExpectedVersion


class DocSignaturesPrepare200Response(UniversalBaseModel):
    signing_id: typing_extensions.Annotated[str, FieldMetadata(alias="signingId"), pydantic.Field(alias="signingId")]
    digest: str
    algorithm: DocSignaturesPrepare200ResponseAlgorithm
    byte_range: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="byteRange"), pydantic.Field(alias="byteRange")
    ]
    contents_size: typing_extensions.Annotated[
        int, FieldMetadata(alias="contentsSize"), pydantic.Field(alias="contentsSize")
    ]
    sub_filter: typing_extensions.Annotated[str, FieldMetadata(alias="subFilter"), pydantic.Field(alias="subFilter")]
    expected_version: typing_extensions.Annotated[
        DocSignaturesPrepare200ResponseExpectedVersion,
        FieldMetadata(alias="expectedVersion"),
        pydantic.Field(alias="expectedVersion"),
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

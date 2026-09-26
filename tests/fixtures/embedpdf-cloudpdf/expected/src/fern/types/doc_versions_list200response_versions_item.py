

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_list200response_versions_item_producer import DocVersionsList200ResponseVersionsItemProducer


class DocVersionsList200ResponseVersionsItem(UniversalBaseModel):
    sha256: str
    byte_length: typing_extensions.Annotated[int, FieldMetadata(alias="byteLength"), pydantic.Field(alias="byteLength")]
    number: int
    parent_sha256: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentSha256"), pydantic.Field(alias="parentSha256")
    ] = None
    producer: DocVersionsList200ResponseVersionsItemProducer
    signing_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="signingId"), pydantic.Field(alias="signingId")
    ] = None
    created_at: typing_extensions.Annotated[int, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

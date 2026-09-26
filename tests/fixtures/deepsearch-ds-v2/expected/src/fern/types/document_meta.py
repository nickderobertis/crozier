

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_server_fastapi_server_public_models_data_indices_upload_models_identifier import (
    ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier,
)
from .document_description import DocumentDescription


class DocumentMeta(UniversalBaseModel):
    filename: typing.Optional[str] = None
    description: typing.Optional[DocumentDescription] = None
    identifiers: typing.Optional[typing.List[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

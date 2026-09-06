

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_paged_response_metadata import ApiPagedResponseMetadata
from .authorization_codes_shared_models_authorization_contact_information import (
    AuthorizationCodesSharedModelsAuthorizationContactInformation,
)


class ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation(UniversalBaseModel):
    entities: typing_extensions.Annotated[
        typing.Optional[typing.List[AuthorizationCodesSharedModelsAuthorizationContactInformation]],
        FieldMetadata(alias="Entities"),
        pydantic.Field(alias="Entities"),
    ] = None
    metadata: typing_extensions.Annotated[
        typing.Optional[ApiPagedResponseMetadata], FieldMetadata(alias="Metadata"), pydantic.Field(alias="Metadata")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

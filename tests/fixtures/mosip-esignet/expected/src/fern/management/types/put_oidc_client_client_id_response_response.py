

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .put_oidc_client_client_id_response_response_status import PutOidcClientClientIdResponseResponseStatus


class PutOidcClientClientIdResponseResponse(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId", description="OIDC client identifier.")
    ]
    """
    OIDC client identifier.
    """

    status: typing.Optional[PutOidcClientClientIdResponseResponseStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .patch_client_client_id_response_response_status import PatchClientClientIdResponseResponseStatus


class PatchClientClientIdResponseResponse(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId", description="Client identifier.")
    ]
    """
    Client identifier.
    """

    status: typing.Optional[PatchClientClientIdResponseResponseStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

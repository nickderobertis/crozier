

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .context_description import ContextDescription
from .context_uuid import ContextUuid
from .required_auth import RequiredAuth


class ContextsResponseItem(UniversalBaseModel):
    context_uuid: typing_extensions.Annotated[
        typing.Optional[ContextUuid], FieldMetadata(alias="context-uuid"), pydantic.Field(alias="context-uuid")
    ] = None
    deletion_required_auths: typing.Optional[RequiredAuth] = None
    export_required_auths: typing.Optional[RequiredAuth] = None
    context_description: typing.Optional[ContextDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

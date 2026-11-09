

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuditActorInfoDto(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Identifier of the actor
    """

    legal_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="legalId"),
        pydantic.Field(alias="legalId", description="Legal entity identifier of the actor"),
    ]
    """
    Legal entity identifier of the actor
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the actor
    """

    external_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="externalId"),
        pydantic.Field(alias="externalId", description="External identifier of the actor, if applicable"),
    ] = None
    """
    External identifier of the actor, if applicable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

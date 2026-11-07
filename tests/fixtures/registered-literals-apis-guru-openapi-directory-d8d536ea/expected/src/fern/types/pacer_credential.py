

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PacerCredential(UniversalBaseModel):
    default_pacer_client_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="defaultPacerClientCode"),
        pydantic.Field(alias="defaultPacerClientCode", description="Pacer Client Code."),
    ] = None
    """
    Pacer Client Code.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    pacer_user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="pacerUserId"), pydantic.Field(alias="pacerUserId", description="Pacer User Id.")
    ]
    """
    Pacer User Id.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

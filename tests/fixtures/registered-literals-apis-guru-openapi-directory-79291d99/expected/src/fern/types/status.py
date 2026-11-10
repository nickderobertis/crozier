

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Status(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    status_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StatusCode"),
        pydantic.Field(alias="StatusCode", description="Satus Code."),
    ] = None
    """
    Satus Code.
    """

    status_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StatusDescription"),
        pydantic.Field(alias="StatusDescription", description="Status Description."),
    ] = None
    """
    Status Description.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

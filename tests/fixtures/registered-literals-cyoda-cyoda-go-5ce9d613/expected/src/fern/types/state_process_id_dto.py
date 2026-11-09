

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StateProcessIdDto(UniversalBaseModel):
    persisted: bool = pydantic.Field()
    """
    Whether the process is persisted
    """

    runtime_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="runtimeId"), pydantic.Field(alias="runtimeId", description="Runtime identifier")
    ]
    """
    Runtime identifier
    """

    persisted_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="persistedId"),
        pydantic.Field(alias="persistedId", description="Persisted identifier, if applicable"),
    ] = None
    """
    Persisted identifier, if applicable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

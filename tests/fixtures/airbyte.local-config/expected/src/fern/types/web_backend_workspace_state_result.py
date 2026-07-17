

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WebBackendWorkspaceStateResult(UniversalBaseModel):
    has_connections: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasConnections"), pydantic.Field(alias="hasConnections")
    ]
    has_destinations: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasDestinations"), pydantic.Field(alias="hasDestinations")
    ]
    has_sources: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasSources"), pydantic.Field(alias="hasSources")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

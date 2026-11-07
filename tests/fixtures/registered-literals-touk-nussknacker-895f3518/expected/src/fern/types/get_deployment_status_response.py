

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetDeploymentStatusResponse(UniversalBaseModel):
    name: str
    problem_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="problemDescription"), pydantic.Field(alias="problemDescription")
    ] = None
    modified_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

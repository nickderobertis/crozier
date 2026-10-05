

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ErrorNode(UniversalBaseModel):
    id: str
    taxonomy_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="taxonomyName"), pydantic.Field(alias="taxonomyName")
    ]
    branch_name: typing_extensions.Annotated[str, FieldMetadata(alias="branchName"), pydantic.Field(alias="branchName")]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    warnings: typing.List[str]
    errors: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

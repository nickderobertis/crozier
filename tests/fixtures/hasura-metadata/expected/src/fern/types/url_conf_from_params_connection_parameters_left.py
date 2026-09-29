

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pg_connection_params import PgConnectionParams


class UrlConfFromParamsConnectionParametersLeft(UniversalBaseModel):
    left: typing_extensions.Annotated[PgConnectionParams, FieldMetadata(alias="Left"), pydantic.Field(alias="Left")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .secret_filter_body import SecretFilterBody
from .secret_scope import SecretScope
from .secret_type import SecretType


class ScopedSecretResultBody(UniversalBaseModel):
    filters: typing.Optional[typing.List[SecretFilterBody]] = None
    id: typing.Optional[str] = None
    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    notes: typing.Optional[str] = None
    scope: typing.Optional[SecretScope] = None
    secret_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="secretName"), pydantic.Field(alias="secretName")
    ] = None
    type: typing.Optional[SecretType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

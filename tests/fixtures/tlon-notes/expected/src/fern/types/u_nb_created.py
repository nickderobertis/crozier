

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notebook import Notebook
from .u_nb_created_visibility import UNbCreatedVisibility


class UNbCreated(UniversalBaseModel):
    host: str
    flag_name: typing_extensions.Annotated[str, FieldMetadata(alias="flagName"), pydantic.Field(alias="flagName")]
    notebook: Notebook
    visibility: UNbCreatedVisibility

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

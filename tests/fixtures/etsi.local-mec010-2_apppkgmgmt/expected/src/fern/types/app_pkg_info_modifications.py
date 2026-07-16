

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_pkg_info_modifications_operation_state import AppPkgInfoModificationsOperationState


class AppPkgInfoModifications(UniversalBaseModel):
    """
    'The data type represents the operational state for an application package resource'
    """

    operation_state: typing_extensions.Annotated[
        AppPkgInfoModificationsOperationState,
        FieldMetadata(alias="operationState"),
        pydantic.Field(alias="operationState"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

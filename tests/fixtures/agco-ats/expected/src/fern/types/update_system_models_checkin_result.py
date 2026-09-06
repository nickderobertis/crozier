

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_package import UpdateSystemModelsPackage


class UpdateSystemModelsCheckinResult(UniversalBaseModel):
    next_transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextTransactionID"),
        pydantic.Field(alias="NextTransactionID", description="The transaction ID to use for the next checkin."),
    ] = None
    """
    The transaction ID to use for the next checkin.
    """

    packages: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsPackage]],
        FieldMetadata(alias="Packages"),
        pydantic.Field(alias="Packages", description="The packages for the client to run."),
    ] = None
    """
    The packages for the client to run.
    """

    remove_packages: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="RemovePackages"),
        pydantic.Field(alias="RemovePackages", description="The package ids for the client to remove."),
    ] = None
    """
    The package ids for the client to remove.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

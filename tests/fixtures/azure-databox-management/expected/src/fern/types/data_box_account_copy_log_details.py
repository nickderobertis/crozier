

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .copy_log_details import CopyLogDetails


class DataBoxAccountCopyLogDetails(CopyLogDetails):
    """
    Copy log details for a storage account of a DataBox job
    """

    account_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountName"),
        pydantic.Field(alias="accountName", description="Destination account name."),
    ] = None
    """
    Destination account name.
    """

    copy_log_link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="copyLogLink"),
        pydantic.Field(alias="copyLogLink", description="Link for copy logs."),
    ] = None
    """
    Link for copy logs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RecordsUploadSmartImportRecordResponse(UniversalBaseModel):
    record_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="recordId"),
        pydantic.Field(alias="recordId", description="Record ID of the new created record"),
    ] = None
    """
    Record ID of the new created record
    """

    import_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="importId"), pydantic.Field(alias="importId")
    ] = None
    remaining_credits: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="remainingCredits"), pydantic.Field(alias="remainingCredits")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

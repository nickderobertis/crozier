

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class RecordsCreateRecordRequestParent(UniversalBaseModel):
    """
    Object containing Record IDs or Ironclad IDs to be set as the parent of the current record.
    """

    record_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="recordId"), pydantic.Field(alias="recordId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

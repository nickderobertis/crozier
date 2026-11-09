

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntityTransactionResponseError(UniversalBaseModel):
    """
    Present only on chunk-failure elements. Absent on successful
    elements (which carry `transactionId` + `entityIds`).
    """

    code: str = pydantic.Field()
    """
    AppError code (e.g. MODEL_NOT_FOUND, ENTITY_NOT_FOUND).
    """

    message: str = pydantic.Field()
    """
    Operator-facing failure message; safe for client display.
    """

    chunk_index: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="chunkIndex"),
        pydantic.Field(alias="chunkIndex", description="Zero-based index of the failing chunk in the response array."),
    ]
    """
    Zero-based index of the failing chunk in the response array.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

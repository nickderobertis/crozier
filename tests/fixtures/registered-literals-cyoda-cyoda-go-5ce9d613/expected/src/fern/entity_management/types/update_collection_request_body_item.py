

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UpdateCollectionRequestBodyItem(UniversalBaseModel):
    id: str
    payload: str
    transition: typing.Optional[str] = None
    if_match: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ifMatch"),
        pydantic.Field(
            alias="ifMatch",
            description="Optional cross-request optimistic-concurrency\nprecondition; cyoda-go extension #228 (not yet in\nCloud).",
        ),
    ] = None
    """
    Optional cross-request optimistic-concurrency
    precondition; cyoda-go extension #228 (not yet in
    Cloud).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ANoteUpdate(UniversalBaseModel):
    body: str
    expected_revision: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="expectedRevision"),
        pydantic.Field(
            alias="expectedRevision",
            description="Server-known revision the client is updating from.\nMismatch surfaces as a `conflict` error (planned;\ncurrently `unknown`).",
        ),
    ]
    """
    Server-known revision the client is updating from.
    Mismatch surfaces as a `conflict` error (planned;
    currently `unknown`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

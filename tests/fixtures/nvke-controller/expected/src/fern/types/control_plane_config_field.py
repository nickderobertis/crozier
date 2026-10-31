

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ControlPlaneConfigField(UniversalBaseModel):
    """
    One field that changed between two snapshots. Values are JSON-encoded.
    """

    field: str = pydantic.Field()
    """
    The field that changed.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="JSON-encoded previous value. Omitted for the first entry."),
    ] = None
    """
    JSON-encoded previous value. Omitted for the first entry.
    """

    to: str = pydantic.Field()
    """
    JSON-encoded new value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

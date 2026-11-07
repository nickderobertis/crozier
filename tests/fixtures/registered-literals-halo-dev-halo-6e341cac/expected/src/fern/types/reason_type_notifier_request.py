

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReasonTypeNotifierRequest(UniversalBaseModel):
    """
    Notifier selection for one reason type.
    """

    notifiers: typing.List[str] = pydantic.Field()
    """
    <code>metadata.name</code> values of enabled notifiers.
    """

    reason_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="reasonType"),
        pydantic.Field(alias="reasonType", description="<code>metadata.name</code> of the reason type."),
    ]
    """
    <code>metadata.name</code> of the reason type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

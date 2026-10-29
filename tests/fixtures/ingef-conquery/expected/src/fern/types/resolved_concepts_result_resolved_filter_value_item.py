

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResolvedConceptsResultResolvedFilterValueItem(UniversalBaseModel):
    value: str = pydantic.Field()
    """
    Actual value - can be treated as the Id of the value. To be used when querying the Filter.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Verbose description of the value.
    """

    option_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="optionValue"),
        pydantic.Field(alias="optionValue", description="Less verbose description of the value."),
    ] = None
    """
    Less verbose description of the value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

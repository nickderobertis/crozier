

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .form import Form


class Complex(UniversalBaseModel):
    """
    An impedance reading in the requested form.
    """

    complex_: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="complex"),
        pydantic.Field(alias="complex", description="Real and imaginary parts, in ohms."),
    ]
    """
    Real and imaginary parts, in ohms.
    """

    form: Form
    str: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reading as the analyser prints it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

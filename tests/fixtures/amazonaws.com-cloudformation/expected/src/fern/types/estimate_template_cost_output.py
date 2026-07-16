

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EstimateTemplateCostOutput(UniversalBaseModel):
    """
    The output for a <a>EstimateTemplateCost</a> action.
    """

    url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Url")] = pydantic.Field(default=None)
    """
    An Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

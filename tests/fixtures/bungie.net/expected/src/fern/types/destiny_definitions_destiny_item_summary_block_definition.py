

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemSummaryBlockDefinition(UniversalBaseModel):
    """
    This appears to be information used when rendering rewards. We don't currently use it on BNet.
    """

    sort_priority: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sortPriority"),
        pydantic.Field(
            alias="sortPriority",
            description="Apparently when rendering an item in a reward, this should be used as a sort priority. We're not doing it presently.",
        ),
    ] = None
    """
    Apparently when rendering an item in a reward, this should be used as a sort priority. We're not doing it presently.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

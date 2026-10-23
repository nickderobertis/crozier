

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DatasetSegyV1Legal(UniversalBaseModel):
    """
    Legal meta data like legal tags, relevant other countries, legal status. This structure is included by the SystemProperties "legal", which is part of all OSDU records. Not extensible.
    """

    legaltags: typing.List[str] = pydantic.Field()
    """
    The list of legal tags, which resolve to legal properties (like country of origin, export classification code, etc.) and rules with the help of the Compliance Service.
    """

    other_relevant_data_countries: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="otherRelevantDataCountries"),
        pydantic.Field(
            alias="otherRelevantDataCountries",
            description="The list of other relevant data countries as an array of two-letter country codes, see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.",
        ),
    ]
    """
    The list of other relevant data countries as an array of two-letter country codes, see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The legal status. Set by the system after evaluation against the compliance rules associated with the "legaltags" using the Compliance Service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

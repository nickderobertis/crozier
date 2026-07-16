

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaxIds(UniversalBaseModel):
    """
    The tax IDs that a Location is operating under.
    """

    eu_vat: typing.Optional[str] = pydantic.Field(default=None)
    """
    The EU VAT number for this location. For example, "IE3426675K".
    If the EU VAT number is present, it is well-formed and has been
    validated with VIES, the VAT Information Exchange System.
    """

    fr_naf: typing.Optional[str] = pydantic.Field(default=None)
    """
    The French government uses the NAF (Nomenclature des Activités Françaises) to display and
    track economic statistical data. This is also called the APE (Activite Principale de l’Entreprise) code.
    For example, 6910Z.
    """

    fr_siret: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SIRET (Système d'Identification du Répertoire des Entreprises et de leurs Etablissements)
    number is a 14 digits code issued by the French INSEE. For example, "39922799000021".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

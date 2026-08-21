

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Medication(UniversalBaseModel):
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="_id"), pydantic.Field(alias="_id")] = (
        None
    )
    subst_ncia: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="SUBSTÂNCIA"), pydantic.Field(alias="SUBSTÂNCIA")
    ] = None
    cnpj: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CNPJ"), pydantic.Field(alias="CNPJ")
    ] = None
    laborat_rio: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LABORATÓRIO"), pydantic.Field(alias="LABORATÓRIO")
    ] = None
    c_digo_ggrem: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CÓDIGO GGREM"), pydantic.Field(alias="CÓDIGO GGREM")
    ] = None
    registro: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="REGISTRO"), pydantic.Field(alias="REGISTRO")
    ] = None
    ean_1: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="EAN 1"), pydantic.Field(alias="EAN 1")
    ] = None
    ean_2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="EAN 2"), pydantic.Field(alias="EAN 2")
    ] = None
    ean_3: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="EAN 3"), pydantic.Field(alias="EAN 3")
    ] = None
    produto: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PRODUTO"), pydantic.Field(alias="PRODUTO")
    ] = None
    apresenta_o: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="APRESENTAÇÃO"), pydantic.Field(alias="APRESENTAÇÃO")
    ] = None
    classe_terap_utica: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CLASSE TERAPÊUTICA"), pydantic.Field(alias="CLASSE TERAPÊUTICA")
    ] = None
    tipo_de_produto_status_do_produto: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TIPO DE PRODUTO (STATUS DO PRODUTO)"),
        pydantic.Field(alias="TIPO DE PRODUTO (STATUS DO PRODUTO)"),
    ] = None
    regime_de_pre_o: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="REGIME DE PREÇO"), pydantic.Field(alias="REGIME DE PREÇO")
    ] = None
    pf_sem_impostos: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF Sem Impostos"), pydantic.Field(alias="PF Sem Impostos")
    ] = None
    pf_0: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 0%"), pydantic.Field(alias="PF 0%")
    ] = None
    pf_12: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 12%"), pydantic.Field(alias="PF 12%")
    ] = None
    pf_17: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 17%"), pydantic.Field(alias="PF 17%")
    ] = None
    pf_17_alc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 17% ALC"), pydantic.Field(alias="PF 17% ALC")
    ] = None
    pf_175: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 17,5%"), pydantic.Field(alias="PF 17,5%")
    ] = None
    pf_175_alc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 17,5% ALC"), pydantic.Field(alias="PF 17,5% ALC")
    ] = None
    pf_18: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 18%"), pydantic.Field(alias="PF 18%")
    ] = None
    pf_18_alc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 18% ALC"), pydantic.Field(alias="PF 18% ALC")
    ] = None
    pf_20: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PF 20%"), pydantic.Field(alias="PF 20%")
    ] = None
    pmc_0: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 0%"), pydantic.Field(alias="PMC 0%")
    ] = None
    pmc_12: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 12%"), pydantic.Field(alias="PMC 12%")
    ] = None
    pmc_17: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 17%"), pydantic.Field(alias="PMC 17%")
    ] = None
    pmc_17_alc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 17% ALC"), pydantic.Field(alias="PMC 17% ALC")
    ] = None
    pmc_175: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 17,5%"), pydantic.Field(alias="PMC 17,5%")
    ] = None
    pmc_175_alc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 17,5% ALC"), pydantic.Field(alias="PMC 17,5% ALC")
    ] = None
    pmc_18: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 18%"), pydantic.Field(alias="PMC 18%")
    ] = None
    pmc_18_alc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 18% ALC"), pydantic.Field(alias="PMC 18% ALC")
    ] = None
    pmc_20: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PMC 20%"), pydantic.Field(alias="PMC 20%")
    ] = None
    restri_o_hospitalar: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="RESTRIÇÃO HOSPITALAR"), pydantic.Field(alias="RESTRIÇÃO HOSPITALAR")
    ] = None
    cap: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="CAP"), pydantic.Field(alias="CAP")] = (
        None
    )
    confaz_87: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CONFAZ 87"), pydantic.Field(alias="CONFAZ 87")
    ] = None
    icms_0: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ICMS 0%"), pydantic.Field(alias="ICMS 0%")
    ] = None
    an_lise_recursal: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ANÁLISE RECURSAL"), pydantic.Field(alias="ANÁLISE RECURSAL")
    ] = None
    lista_de_concess_o_de_cr_dito_tribut_rio_pis_cofins: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)"),
        pydantic.Field(alias="LISTA DE CONCESSÃO DE CRÉDITO TRIBUTÁRIO (PIS/COFINS)"),
    ] = None
    comercializa_o_2019: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="COMERCIALIZAÇÃO 2019"), pydantic.Field(alias="COMERCIALIZAÇÃO 2019")
    ] = None
    tarja: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="TARJA"), pydantic.Field(alias="TARJA")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

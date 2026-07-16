

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem(str, enum.Enum):
    """
    Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.
    Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd
    """

    GEAS = "GEAS"
    GEBA = "GEBA"
    GEBR = "GEBR"
    GEBU = "GEBU"
    GECI = "GECI"
    GECS = "GECS"
    GEFB = "GEFB"
    GEFG = "GEFG"
    GEG = "GEG"
    GEGR = "GEGR"
    GEGS = "GEGS"
    GEOT = "GEOT"
    GEOV = "GEOV"
    GEPA = "GEPA"
    GEPR = "GEPR"
    GERE = "GERE"
    GEST = "GEST"
    GEYA = "GEYA"
    GEYO = "GEYO"
    PSCA = "PSCA"
    PSES = "PSES"
    PSNC = "PSNC"
    PSNP = "PSNP"
    PSRG = "PSRG"
    PSSS = "PSSS"
    PSST = "PSST"
    PSSW = "PSSW"

    def visit(
        self,
        geas: typing.Callable[[], T_Result],
        geba: typing.Callable[[], T_Result],
        gebr: typing.Callable[[], T_Result],
        gebu: typing.Callable[[], T_Result],
        geci: typing.Callable[[], T_Result],
        gecs: typing.Callable[[], T_Result],
        gefb: typing.Callable[[], T_Result],
        gefg: typing.Callable[[], T_Result],
        geg: typing.Callable[[], T_Result],
        gegr: typing.Callable[[], T_Result],
        gegs: typing.Callable[[], T_Result],
        geot: typing.Callable[[], T_Result],
        geov: typing.Callable[[], T_Result],
        gepa: typing.Callable[[], T_Result],
        gepr: typing.Callable[[], T_Result],
        gere: typing.Callable[[], T_Result],
        gest: typing.Callable[[], T_Result],
        geya: typing.Callable[[], T_Result],
        geyo: typing.Callable[[], T_Result],
        psca: typing.Callable[[], T_Result],
        pses: typing.Callable[[], T_Result],
        psnc: typing.Callable[[], T_Result],
        psnp: typing.Callable[[], T_Result],
        psrg: typing.Callable[[], T_Result],
        psss: typing.Callable[[], T_Result],
        psst: typing.Callable[[], T_Result],
        pssw: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEAS:
            return geas()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEBA:
            return geba()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEBR:
            return gebr()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEBU:
            return gebu()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GECI:
            return geci()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GECS:
            return gecs()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEFB:
            return gefb()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEFG:
            return gefg()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEG:
            return geg()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEGR:
            return gegr()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEGS:
            return gegs()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEOT:
            return geot()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEOV:
            return geov()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEPA:
            return gepa()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEPR:
            return gepr()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GERE:
            return gere()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEST:
            return gest()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEYA:
            return geya()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.GEYO:
            return geyo()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSCA:
            return psca()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSES:
            return pses()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSNC:
            return psnc()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSNP:
            return psnp()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSRG:
            return psrg()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSSS:
            return psss()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSST:
            return psst()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem.PSSW:
            return pssw()

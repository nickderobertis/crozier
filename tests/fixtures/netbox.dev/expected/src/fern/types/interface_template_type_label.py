

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfaceTemplateTypeLabel(str, enum.Enum):
    VIRTUAL = "Virtual"
    BRIDGE = "Bridge"
    LINK_AGGREGATION_GROUP_LAG = "Link Aggregation Group (LAG)"
    ONE_HUNDRED_BASE_FX10100ME_FIBER = "100BASE-FX (10/100ME FIBER)"
    ONE_HUNDRED_BASE_LFX10100ME_FIBER = "100BASE-LFX (10/100ME FIBER)"
    ONE_HUNDRED_BASE_TX10100ME = "100BASE-TX (10/100ME)"
    ONE_HUNDRED_BASE_T110100ME_SINGLE_PAIR = "100BASE-T1 (10/100ME Single Pair)"
    ONE_THOUSAND_BASE_T1GE = "1000BASE-T (1GE)"
    TWO5GBASE_T25GE = "2.5GBASE-T (2.5GE)"
    FIVE_GBASE_T5GE = "5GBASE-T (5GE)"
    TEN_GBASE_T10GE = "10GBASE-T (10GE)"
    TEN_GBASE_CX410GE = "10GBASE-CX4 (10GE)"
    GBIC1GE = "GBIC (1GE)"
    SFP1GE = "SFP (1GE)"
    SFP10GE = "SFP+ (10GE)"
    XFP10GE = "XFP (10GE)"
    XENPAK10GE = "XENPAK (10GE)"
    X210GE = "X2 (10GE)"
    SFP2825GE = "SFP28 (25GE)"
    SFP5650GE = "SFP56 (50GE)"
    QSFP40GE = "QSFP+ (40GE)"
    QSFP2850GE = "QSFP28 (50GE)"
    CFP100GE = "CFP (100GE)"
    CFP2100GE = "CFP2 (100GE)"
    CFP2200GE = "CFP2 (200GE)"
    CFP4100GE = "CFP4 (100GE)"
    CISCO_CPAK100GE = "Cisco CPAK (100GE)"
    QSFP28100GE = "QSFP28 (100GE)"
    QSFP56200GE = "QSFP56 (200GE)"
    QSFP_DD400GE = "QSFP-DD (400GE)"
    OSFP400GE = "OSFP (400GE)"
    QSFP_DD800GE = "QSFP-DD (800GE)"
    OSFP800GE = "OSFP (800GE)"
    ONE_THOUSAND_BASE_KX1GE = "1000BASE-KX (1GE)"
    TEN_GBASE_KR10GE = "10GBASE-KR (10GE)"
    TEN_GBASE_KX410GE = "10GBASE-KX4 (10GE)"
    TWENTY_FIVE_GBASE_KR25GE = "25GBASE-KR (25GE)"
    FORTY_GBASE_KR440GE = "40GBASE-KR4 (40GE)"
    FIFTY_GBASE_KR50GE = "50GBASE-KR (50GE)"
    ONE_HUNDRED_GBASE_KP4100GE = "100GBASE-KP4 (100GE)"
    ONE_HUNDRED_GBASE_KR2100GE = "100GBASE-KR2 (100GE)"
    ONE_HUNDRED_GBASE_KR4100GE = "100GBASE-KR4 (100GE)"
    IEEE80211A = "IEEE 802.11a"
    IEEE80211BG = "IEEE 802.11b/g"
    IEEE80211N = "IEEE 802.11n"
    IEEE80211AC = "IEEE 802.11ac"
    IEEE80211AD = "IEEE 802.11ad"
    IEEE80211AX = "IEEE 802.11ax"
    IEEE80211AY = "IEEE 802.11ay"
    IEEE802151BLUETOOTH = "IEEE 802.15.1 (Bluetooth)"
    OTHER_WIRELESS = "Other (Wireless)"
    GSM = "GSM"
    CDMA = "CDMA"
    LTE = "LTE"
    OC3STM1 = "OC-3/STM-1"
    OC12STM4 = "OC-12/STM-4"
    OC48STM16 = "OC-48/STM-16"
    OC192STM64 = "OC-192/STM-64"
    OC768STM256 = "OC-768/STM-256"
    OC1920STM640 = "OC-1920/STM-640"
    OC3840STM1234 = "OC-3840/STM-1234"
    SFP1GFC = "SFP (1GFC)"
    SFP2GFC = "SFP (2GFC)"
    SFP4GFC = "SFP (4GFC)"
    SFP8GFC = "SFP+ (8GFC)"
    SFP16GFC = "SFP+ (16GFC)"
    SFP2832GFC = "SFP28 (32GFC)"
    QSFP64GFC = "QSFP+ (64GFC)"
    QSFP28128GFC = "QSFP28 (128GFC)"
    SDR2GBPS = "SDR (2 Gbps)"
    DDR4GBPS = "DDR (4 Gbps)"
    QDR8GBPS = "QDR (8 Gbps)"
    FDR1010GBPS = "FDR10 (10 Gbps)"
    FDR135GBPS = "FDR (13.5 Gbps)"
    EDR25GBPS = "EDR (25 Gbps)"
    HDR50GBPS = "HDR (50 Gbps)"
    NDR100GBPS = "NDR (100 Gbps)"
    XDR250GBPS = "XDR (250 Gbps)"
    T11544MBPS = "T1 (1.544 Mbps)"
    E12048MBPS = "E1 (2.048 Mbps)"
    T345MBPS = "T3 (45 Mbps)"
    E334MBPS = "E3 (34 Mbps)"
    X_DSL = "xDSL"
    DOCSIS = "DOCSIS"
    GPON25GBPS125GPS = "GPON (2.5 Gbps / 1.25 Gps)"
    XG_PON10GBPS25GBPS = "XG-PON (10 Gbps / 2.5 Gbps)"
    XGS_PON10GBPS = "XGS-PON (10 Gbps)"
    NG_PON2TWDM_PON4X10GBPS = "NG-PON2 (TWDM-PON) (4x10 Gbps)"
    EPON1GBPS = "EPON (1 Gbps)"
    TEN_G_EPON10GBPS = "10G-EPON (10 Gbps)"
    CISCO_STACK_WISE = "Cisco StackWise"
    CISCO_STACK_WISE_PLUS = "Cisco StackWise Plus"
    CISCO_FLEX_STACK = "Cisco FlexStack"
    CISCO_FLEX_STACK_PLUS = "Cisco FlexStack Plus"
    CISCO_STACK_WISE80 = "Cisco StackWise-80"
    CISCO_STACK_WISE160 = "Cisco StackWise-160"
    CISCO_STACK_WISE320 = "Cisco StackWise-320"
    CISCO_STACK_WISE480 = "Cisco StackWise-480"
    CISCO_STACK_WISE1T = "Cisco StackWise-1T"
    JUNIPER_VCP = "Juniper VCP"
    EXTREME_SUMMIT_STACK = "Extreme SummitStack"
    EXTREME_SUMMIT_STACK128 = "Extreme SummitStack-128"
    EXTREME_SUMMIT_STACK256 = "Extreme SummitStack-256"
    EXTREME_SUMMIT_STACK512 = "Extreme SummitStack-512"
    OTHER = "Other"

    def visit(
        self,
        virtual: typing.Callable[[], T_Result],
        bridge: typing.Callable[[], T_Result],
        link_aggregation_group_lag: typing.Callable[[], T_Result],
        one_hundred_base_fx10100me_fiber: typing.Callable[[], T_Result],
        one_hundred_base_lfx10100me_fiber: typing.Callable[[], T_Result],
        one_hundred_base_tx10100me: typing.Callable[[], T_Result],
        one_hundred_base_t110100me_single_pair: typing.Callable[[], T_Result],
        one_thousand_base_t1ge: typing.Callable[[], T_Result],
        two5gbase_t25ge: typing.Callable[[], T_Result],
        five_gbase_t5ge: typing.Callable[[], T_Result],
        ten_gbase_t10ge: typing.Callable[[], T_Result],
        ten_gbase_cx410ge: typing.Callable[[], T_Result],
        gbic1ge: typing.Callable[[], T_Result],
        sfp1ge: typing.Callable[[], T_Result],
        sfp10ge: typing.Callable[[], T_Result],
        xfp10ge: typing.Callable[[], T_Result],
        xenpak10ge: typing.Callable[[], T_Result],
        x210ge: typing.Callable[[], T_Result],
        sfp2825ge: typing.Callable[[], T_Result],
        sfp5650ge: typing.Callable[[], T_Result],
        qsfp40ge: typing.Callable[[], T_Result],
        qsfp2850ge: typing.Callable[[], T_Result],
        cfp100ge: typing.Callable[[], T_Result],
        cfp2100ge: typing.Callable[[], T_Result],
        cfp2200ge: typing.Callable[[], T_Result],
        cfp4100ge: typing.Callable[[], T_Result],
        cisco_cpak100ge: typing.Callable[[], T_Result],
        qsfp28100ge: typing.Callable[[], T_Result],
        qsfp56200ge: typing.Callable[[], T_Result],
        qsfp_dd400ge: typing.Callable[[], T_Result],
        osfp400ge: typing.Callable[[], T_Result],
        qsfp_dd800ge: typing.Callable[[], T_Result],
        osfp800ge: typing.Callable[[], T_Result],
        one_thousand_base_kx1ge: typing.Callable[[], T_Result],
        ten_gbase_kr10ge: typing.Callable[[], T_Result],
        ten_gbase_kx410ge: typing.Callable[[], T_Result],
        twenty_five_gbase_kr25ge: typing.Callable[[], T_Result],
        forty_gbase_kr440ge: typing.Callable[[], T_Result],
        fifty_gbase_kr50ge: typing.Callable[[], T_Result],
        one_hundred_gbase_kp4100ge: typing.Callable[[], T_Result],
        one_hundred_gbase_kr2100ge: typing.Callable[[], T_Result],
        one_hundred_gbase_kr4100ge: typing.Callable[[], T_Result],
        ieee80211a: typing.Callable[[], T_Result],
        ieee80211bg: typing.Callable[[], T_Result],
        ieee80211n: typing.Callable[[], T_Result],
        ieee80211ac: typing.Callable[[], T_Result],
        ieee80211ad: typing.Callable[[], T_Result],
        ieee80211ax: typing.Callable[[], T_Result],
        ieee80211ay: typing.Callable[[], T_Result],
        ieee802151bluetooth: typing.Callable[[], T_Result],
        other_wireless: typing.Callable[[], T_Result],
        gsm: typing.Callable[[], T_Result],
        cdma: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
        oc3stm1: typing.Callable[[], T_Result],
        oc12stm4: typing.Callable[[], T_Result],
        oc48stm16: typing.Callable[[], T_Result],
        oc192stm64: typing.Callable[[], T_Result],
        oc768stm256: typing.Callable[[], T_Result],
        oc1920stm640: typing.Callable[[], T_Result],
        oc3840stm1234: typing.Callable[[], T_Result],
        sfp1gfc: typing.Callable[[], T_Result],
        sfp2gfc: typing.Callable[[], T_Result],
        sfp4gfc: typing.Callable[[], T_Result],
        sfp8gfc: typing.Callable[[], T_Result],
        sfp16gfc: typing.Callable[[], T_Result],
        sfp2832gfc: typing.Callable[[], T_Result],
        qsfp64gfc: typing.Callable[[], T_Result],
        qsfp28128gfc: typing.Callable[[], T_Result],
        sdr2gbps: typing.Callable[[], T_Result],
        ddr4gbps: typing.Callable[[], T_Result],
        qdr8gbps: typing.Callable[[], T_Result],
        fdr1010gbps: typing.Callable[[], T_Result],
        fdr135gbps: typing.Callable[[], T_Result],
        edr25gbps: typing.Callable[[], T_Result],
        hdr50gbps: typing.Callable[[], T_Result],
        ndr100gbps: typing.Callable[[], T_Result],
        xdr250gbps: typing.Callable[[], T_Result],
        t11544mbps: typing.Callable[[], T_Result],
        e12048mbps: typing.Callable[[], T_Result],
        t345mbps: typing.Callable[[], T_Result],
        e334mbps: typing.Callable[[], T_Result],
        x_dsl: typing.Callable[[], T_Result],
        docsis: typing.Callable[[], T_Result],
        gpon25gbps125gps: typing.Callable[[], T_Result],
        xg_pon10gbps25gbps: typing.Callable[[], T_Result],
        xgs_pon10gbps: typing.Callable[[], T_Result],
        ng_pon2twdm_pon4x10gbps: typing.Callable[[], T_Result],
        epon1gbps: typing.Callable[[], T_Result],
        ten_g_epon10gbps: typing.Callable[[], T_Result],
        cisco_stack_wise: typing.Callable[[], T_Result],
        cisco_stack_wise_plus: typing.Callable[[], T_Result],
        cisco_flex_stack: typing.Callable[[], T_Result],
        cisco_flex_stack_plus: typing.Callable[[], T_Result],
        cisco_stack_wise80: typing.Callable[[], T_Result],
        cisco_stack_wise160: typing.Callable[[], T_Result],
        cisco_stack_wise320: typing.Callable[[], T_Result],
        cisco_stack_wise480: typing.Callable[[], T_Result],
        cisco_stack_wise1t: typing.Callable[[], T_Result],
        juniper_vcp: typing.Callable[[], T_Result],
        extreme_summit_stack: typing.Callable[[], T_Result],
        extreme_summit_stack128: typing.Callable[[], T_Result],
        extreme_summit_stack256: typing.Callable[[], T_Result],
        extreme_summit_stack512: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfaceTemplateTypeLabel.VIRTUAL:
            return virtual()
        if self is InterfaceTemplateTypeLabel.BRIDGE:
            return bridge()
        if self is InterfaceTemplateTypeLabel.LINK_AGGREGATION_GROUP_LAG:
            return link_aggregation_group_lag()
        if self is InterfaceTemplateTypeLabel.ONE_HUNDRED_BASE_FX10100ME_FIBER:
            return one_hundred_base_fx10100me_fiber()
        if self is InterfaceTemplateTypeLabel.ONE_HUNDRED_BASE_LFX10100ME_FIBER:
            return one_hundred_base_lfx10100me_fiber()
        if self is InterfaceTemplateTypeLabel.ONE_HUNDRED_BASE_TX10100ME:
            return one_hundred_base_tx10100me()
        if self is InterfaceTemplateTypeLabel.ONE_HUNDRED_BASE_T110100ME_SINGLE_PAIR:
            return one_hundred_base_t110100me_single_pair()
        if self is InterfaceTemplateTypeLabel.ONE_THOUSAND_BASE_T1GE:
            return one_thousand_base_t1ge()
        if self is InterfaceTemplateTypeLabel.TWO5GBASE_T25GE:
            return two5gbase_t25ge()
        if self is InterfaceTemplateTypeLabel.FIVE_GBASE_T5GE:
            return five_gbase_t5ge()
        if self is InterfaceTemplateTypeLabel.TEN_GBASE_T10GE:
            return ten_gbase_t10ge()
        if self is InterfaceTemplateTypeLabel.TEN_GBASE_CX410GE:
            return ten_gbase_cx410ge()
        if self is InterfaceTemplateTypeLabel.GBIC1GE:
            return gbic1ge()
        if self is InterfaceTemplateTypeLabel.SFP1GE:
            return sfp1ge()
        if self is InterfaceTemplateTypeLabel.SFP10GE:
            return sfp10ge()
        if self is InterfaceTemplateTypeLabel.XFP10GE:
            return xfp10ge()
        if self is InterfaceTemplateTypeLabel.XENPAK10GE:
            return xenpak10ge()
        if self is InterfaceTemplateTypeLabel.X210GE:
            return x210ge()
        if self is InterfaceTemplateTypeLabel.SFP2825GE:
            return sfp2825ge()
        if self is InterfaceTemplateTypeLabel.SFP5650GE:
            return sfp5650ge()
        if self is InterfaceTemplateTypeLabel.QSFP40GE:
            return qsfp40ge()
        if self is InterfaceTemplateTypeLabel.QSFP2850GE:
            return qsfp2850ge()
        if self is InterfaceTemplateTypeLabel.CFP100GE:
            return cfp100ge()
        if self is InterfaceTemplateTypeLabel.CFP2100GE:
            return cfp2100ge()
        if self is InterfaceTemplateTypeLabel.CFP2200GE:
            return cfp2200ge()
        if self is InterfaceTemplateTypeLabel.CFP4100GE:
            return cfp4100ge()
        if self is InterfaceTemplateTypeLabel.CISCO_CPAK100GE:
            return cisco_cpak100ge()
        if self is InterfaceTemplateTypeLabel.QSFP28100GE:
            return qsfp28100ge()
        if self is InterfaceTemplateTypeLabel.QSFP56200GE:
            return qsfp56200ge()
        if self is InterfaceTemplateTypeLabel.QSFP_DD400GE:
            return qsfp_dd400ge()
        if self is InterfaceTemplateTypeLabel.OSFP400GE:
            return osfp400ge()
        if self is InterfaceTemplateTypeLabel.QSFP_DD800GE:
            return qsfp_dd800ge()
        if self is InterfaceTemplateTypeLabel.OSFP800GE:
            return osfp800ge()
        if self is InterfaceTemplateTypeLabel.ONE_THOUSAND_BASE_KX1GE:
            return one_thousand_base_kx1ge()
        if self is InterfaceTemplateTypeLabel.TEN_GBASE_KR10GE:
            return ten_gbase_kr10ge()
        if self is InterfaceTemplateTypeLabel.TEN_GBASE_KX410GE:
            return ten_gbase_kx410ge()
        if self is InterfaceTemplateTypeLabel.TWENTY_FIVE_GBASE_KR25GE:
            return twenty_five_gbase_kr25ge()
        if self is InterfaceTemplateTypeLabel.FORTY_GBASE_KR440GE:
            return forty_gbase_kr440ge()
        if self is InterfaceTemplateTypeLabel.FIFTY_GBASE_KR50GE:
            return fifty_gbase_kr50ge()
        if self is InterfaceTemplateTypeLabel.ONE_HUNDRED_GBASE_KP4100GE:
            return one_hundred_gbase_kp4100ge()
        if self is InterfaceTemplateTypeLabel.ONE_HUNDRED_GBASE_KR2100GE:
            return one_hundred_gbase_kr2100ge()
        if self is InterfaceTemplateTypeLabel.ONE_HUNDRED_GBASE_KR4100GE:
            return one_hundred_gbase_kr4100ge()
        if self is InterfaceTemplateTypeLabel.IEEE80211A:
            return ieee80211a()
        if self is InterfaceTemplateTypeLabel.IEEE80211BG:
            return ieee80211bg()
        if self is InterfaceTemplateTypeLabel.IEEE80211N:
            return ieee80211n()
        if self is InterfaceTemplateTypeLabel.IEEE80211AC:
            return ieee80211ac()
        if self is InterfaceTemplateTypeLabel.IEEE80211AD:
            return ieee80211ad()
        if self is InterfaceTemplateTypeLabel.IEEE80211AX:
            return ieee80211ax()
        if self is InterfaceTemplateTypeLabel.IEEE80211AY:
            return ieee80211ay()
        if self is InterfaceTemplateTypeLabel.IEEE802151BLUETOOTH:
            return ieee802151bluetooth()
        if self is InterfaceTemplateTypeLabel.OTHER_WIRELESS:
            return other_wireless()
        if self is InterfaceTemplateTypeLabel.GSM:
            return gsm()
        if self is InterfaceTemplateTypeLabel.CDMA:
            return cdma()
        if self is InterfaceTemplateTypeLabel.LTE:
            return lte()
        if self is InterfaceTemplateTypeLabel.OC3STM1:
            return oc3stm1()
        if self is InterfaceTemplateTypeLabel.OC12STM4:
            return oc12stm4()
        if self is InterfaceTemplateTypeLabel.OC48STM16:
            return oc48stm16()
        if self is InterfaceTemplateTypeLabel.OC192STM64:
            return oc192stm64()
        if self is InterfaceTemplateTypeLabel.OC768STM256:
            return oc768stm256()
        if self is InterfaceTemplateTypeLabel.OC1920STM640:
            return oc1920stm640()
        if self is InterfaceTemplateTypeLabel.OC3840STM1234:
            return oc3840stm1234()
        if self is InterfaceTemplateTypeLabel.SFP1GFC:
            return sfp1gfc()
        if self is InterfaceTemplateTypeLabel.SFP2GFC:
            return sfp2gfc()
        if self is InterfaceTemplateTypeLabel.SFP4GFC:
            return sfp4gfc()
        if self is InterfaceTemplateTypeLabel.SFP8GFC:
            return sfp8gfc()
        if self is InterfaceTemplateTypeLabel.SFP16GFC:
            return sfp16gfc()
        if self is InterfaceTemplateTypeLabel.SFP2832GFC:
            return sfp2832gfc()
        if self is InterfaceTemplateTypeLabel.QSFP64GFC:
            return qsfp64gfc()
        if self is InterfaceTemplateTypeLabel.QSFP28128GFC:
            return qsfp28128gfc()
        if self is InterfaceTemplateTypeLabel.SDR2GBPS:
            return sdr2gbps()
        if self is InterfaceTemplateTypeLabel.DDR4GBPS:
            return ddr4gbps()
        if self is InterfaceTemplateTypeLabel.QDR8GBPS:
            return qdr8gbps()
        if self is InterfaceTemplateTypeLabel.FDR1010GBPS:
            return fdr1010gbps()
        if self is InterfaceTemplateTypeLabel.FDR135GBPS:
            return fdr135gbps()
        if self is InterfaceTemplateTypeLabel.EDR25GBPS:
            return edr25gbps()
        if self is InterfaceTemplateTypeLabel.HDR50GBPS:
            return hdr50gbps()
        if self is InterfaceTemplateTypeLabel.NDR100GBPS:
            return ndr100gbps()
        if self is InterfaceTemplateTypeLabel.XDR250GBPS:
            return xdr250gbps()
        if self is InterfaceTemplateTypeLabel.T11544MBPS:
            return t11544mbps()
        if self is InterfaceTemplateTypeLabel.E12048MBPS:
            return e12048mbps()
        if self is InterfaceTemplateTypeLabel.T345MBPS:
            return t345mbps()
        if self is InterfaceTemplateTypeLabel.E334MBPS:
            return e334mbps()
        if self is InterfaceTemplateTypeLabel.X_DSL:
            return x_dsl()
        if self is InterfaceTemplateTypeLabel.DOCSIS:
            return docsis()
        if self is InterfaceTemplateTypeLabel.GPON25GBPS125GPS:
            return gpon25gbps125gps()
        if self is InterfaceTemplateTypeLabel.XG_PON10GBPS25GBPS:
            return xg_pon10gbps25gbps()
        if self is InterfaceTemplateTypeLabel.XGS_PON10GBPS:
            return xgs_pon10gbps()
        if self is InterfaceTemplateTypeLabel.NG_PON2TWDM_PON4X10GBPS:
            return ng_pon2twdm_pon4x10gbps()
        if self is InterfaceTemplateTypeLabel.EPON1GBPS:
            return epon1gbps()
        if self is InterfaceTemplateTypeLabel.TEN_G_EPON10GBPS:
            return ten_g_epon10gbps()
        if self is InterfaceTemplateTypeLabel.CISCO_STACK_WISE:
            return cisco_stack_wise()
        if self is InterfaceTemplateTypeLabel.CISCO_STACK_WISE_PLUS:
            return cisco_stack_wise_plus()
        if self is InterfaceTemplateTypeLabel.CISCO_FLEX_STACK:
            return cisco_flex_stack()
        if self is InterfaceTemplateTypeLabel.CISCO_FLEX_STACK_PLUS:
            return cisco_flex_stack_plus()
        if self is InterfaceTemplateTypeLabel.CISCO_STACK_WISE80:
            return cisco_stack_wise80()
        if self is InterfaceTemplateTypeLabel.CISCO_STACK_WISE160:
            return cisco_stack_wise160()
        if self is InterfaceTemplateTypeLabel.CISCO_STACK_WISE320:
            return cisco_stack_wise320()
        if self is InterfaceTemplateTypeLabel.CISCO_STACK_WISE480:
            return cisco_stack_wise480()
        if self is InterfaceTemplateTypeLabel.CISCO_STACK_WISE1T:
            return cisco_stack_wise1t()
        if self is InterfaceTemplateTypeLabel.JUNIPER_VCP:
            return juniper_vcp()
        if self is InterfaceTemplateTypeLabel.EXTREME_SUMMIT_STACK:
            return extreme_summit_stack()
        if self is InterfaceTemplateTypeLabel.EXTREME_SUMMIT_STACK128:
            return extreme_summit_stack128()
        if self is InterfaceTemplateTypeLabel.EXTREME_SUMMIT_STACK256:
            return extreme_summit_stack256()
        if self is InterfaceTemplateTypeLabel.EXTREME_SUMMIT_STACK512:
            return extreme_summit_stack512()
        if self is InterfaceTemplateTypeLabel.OTHER:
            return other()

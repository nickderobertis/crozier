

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerOutletTemplateTypeLabel(str, enum.Enum):
    C5 = "C5"
    C7 = "C7"
    C13 = "C13"
    C15 = "C15"
    C19 = "C19"
    C21 = "C21"
    PNE4H = "P+N+E 4H"
    PNE6H = "P+N+E 6H"
    PNE9H = "P+N+E 9H"
    TWO_PE4H = "2P+E 4H"
    TWO_PE6H = "2P+E 6H"
    TWO_PE9H = "2P+E 9H"
    THREE_PE4H = "3P+E 4H"
    THREE_PE6H = "3P+E 6H"
    THREE_PE9H = "3P+E 9H"
    THREE_PNE4H = "3P+N+E 4H"
    THREE_PNE6H = "3P+N+E 6H"
    THREE_PNE9H = "3P+N+E 9H"
    NEMA115R = "NEMA 1-15R"
    NEMA515R = "NEMA 5-15R"
    NEMA520R = "NEMA 5-20R"
    NEMA530R = "NEMA 5-30R"
    NEMA550R = "NEMA 5-50R"
    NEMA615R = "NEMA 6-15R"
    NEMA620R = "NEMA 6-20R"
    NEMA630R = "NEMA 6-30R"
    NEMA650R = "NEMA 6-50R"
    NEMA1030R = "NEMA 10-30R"
    NEMA1050R = "NEMA 10-50R"
    NEMA1420R = "NEMA 14-20R"
    NEMA1430R = "NEMA 14-30R"
    NEMA1450R = "NEMA 14-50R"
    NEMA1460R = "NEMA 14-60R"
    NEMA1515R = "NEMA 15-15R"
    NEMA1520R = "NEMA 15-20R"
    NEMA1530R = "NEMA 15-30R"
    NEMA1550R = "NEMA 15-50R"
    NEMA1560R = "NEMA 15-60R"
    NEMA_L115R = "NEMA L1-15R"
    NEMA_L515R = "NEMA L5-15R"
    NEMA_L520R = "NEMA L5-20R"
    NEMA_L530R = "NEMA L5-30R"
    NEMA_L550R = "NEMA L5-50R"
    NEMA_L615R = "NEMA L6-15R"
    NEMA_L620R = "NEMA L6-20R"
    NEMA_L630R = "NEMA L6-30R"
    NEMA_L650R = "NEMA L6-50R"
    NEMA_L1030R = "NEMA L10-30R"
    NEMA_L1420R = "NEMA L14-20R"
    NEMA_L1430R = "NEMA L14-30R"
    NEMA_L1450R = "NEMA L14-50R"
    NEMA_L1460R = "NEMA L14-60R"
    NEMA_L1520R = "NEMA L15-20R"
    NEMA_L1530R = "NEMA L15-30R"
    NEMA_L1550R = "NEMA L15-50R"
    NEMA_L1560R = "NEMA L15-60R"
    NEMA_L2120R = "NEMA L21-20R"
    NEMA_L2130R = "NEMA L21-30R"
    NEMA_L2230R = "NEMA L22-30R"
    CS6360C = "CS6360C"
    CS6364C = "CS6364C"
    CS8164C = "CS8164C"
    CS8264C = "CS8264C"
    CS8364C = "CS8364C"
    CS8464C = "CS8464C"
    ITA_TYPE_E_CEE75 = "ITA Type E (CEE 7/5)"
    ITA_TYPE_F_CEE73 = "ITA Type F (CEE 7/3)"
    ITA_TYPE_G_BS1363 = "ITA Type G (BS 1363)"
    ITA_TYPE_H = "ITA Type H"
    ITA_TYPE_I = "ITA Type I"
    ITA_TYPE_J = "ITA Type J"
    ITA_TYPE_K = "ITA Type K"
    ITA_TYPE_L_CEI2350 = "ITA Type L (CEI 23-50)"
    ITA_TYPE_M_BS546 = "ITA Type M (BS 546)"
    ITA_TYPE_N = "ITA Type N"
    ITA_TYPE_O = "ITA Type O"
    ITA_MULTISTANDARD = "ITA Multistandard"
    USB_TYPE_A = "USB Type A"
    USB_MICRO_B = "USB Micro B"
    USB_TYPE_C = "USB Type C"
    DC_TERMINAL = "DC Terminal"
    HDOT_CX = "HDOT Cx"
    SAF_D_GRID = "Saf-D-Grid"
    NEUTRIK_POWER_CON20A = "Neutrik powerCON (20A)"
    NEUTRIK_POWER_CON32A = "Neutrik powerCON (32A)"
    NEUTRIK_POWER_CON_TRUE1 = "Neutrik powerCON TRUE1"
    NEUTRIK_POWER_CON_TRUE1TOP = "Neutrik powerCON TRUE1 TOP"
    UBIQUITI_SMART_POWER = "Ubiquiti SmartPower"
    HARDWIRED = "Hardwired"
    OTHER = "Other"

    def visit(
        self,
        c5: typing.Callable[[], T_Result],
        c7: typing.Callable[[], T_Result],
        c13: typing.Callable[[], T_Result],
        c15: typing.Callable[[], T_Result],
        c19: typing.Callable[[], T_Result],
        c21: typing.Callable[[], T_Result],
        pne4h: typing.Callable[[], T_Result],
        pne6h: typing.Callable[[], T_Result],
        pne9h: typing.Callable[[], T_Result],
        two_pe4h: typing.Callable[[], T_Result],
        two_pe6h: typing.Callable[[], T_Result],
        two_pe9h: typing.Callable[[], T_Result],
        three_pe4h: typing.Callable[[], T_Result],
        three_pe6h: typing.Callable[[], T_Result],
        three_pe9h: typing.Callable[[], T_Result],
        three_pne4h: typing.Callable[[], T_Result],
        three_pne6h: typing.Callable[[], T_Result],
        three_pne9h: typing.Callable[[], T_Result],
        nema115r: typing.Callable[[], T_Result],
        nema515r: typing.Callable[[], T_Result],
        nema520r: typing.Callable[[], T_Result],
        nema530r: typing.Callable[[], T_Result],
        nema550r: typing.Callable[[], T_Result],
        nema615r: typing.Callable[[], T_Result],
        nema620r: typing.Callable[[], T_Result],
        nema630r: typing.Callable[[], T_Result],
        nema650r: typing.Callable[[], T_Result],
        nema1030r: typing.Callable[[], T_Result],
        nema1050r: typing.Callable[[], T_Result],
        nema1420r: typing.Callable[[], T_Result],
        nema1430r: typing.Callable[[], T_Result],
        nema1450r: typing.Callable[[], T_Result],
        nema1460r: typing.Callable[[], T_Result],
        nema1515r: typing.Callable[[], T_Result],
        nema1520r: typing.Callable[[], T_Result],
        nema1530r: typing.Callable[[], T_Result],
        nema1550r: typing.Callable[[], T_Result],
        nema1560r: typing.Callable[[], T_Result],
        nema_l115r: typing.Callable[[], T_Result],
        nema_l515r: typing.Callable[[], T_Result],
        nema_l520r: typing.Callable[[], T_Result],
        nema_l530r: typing.Callable[[], T_Result],
        nema_l550r: typing.Callable[[], T_Result],
        nema_l615r: typing.Callable[[], T_Result],
        nema_l620r: typing.Callable[[], T_Result],
        nema_l630r: typing.Callable[[], T_Result],
        nema_l650r: typing.Callable[[], T_Result],
        nema_l1030r: typing.Callable[[], T_Result],
        nema_l1420r: typing.Callable[[], T_Result],
        nema_l1430r: typing.Callable[[], T_Result],
        nema_l1450r: typing.Callable[[], T_Result],
        nema_l1460r: typing.Callable[[], T_Result],
        nema_l1520r: typing.Callable[[], T_Result],
        nema_l1530r: typing.Callable[[], T_Result],
        nema_l1550r: typing.Callable[[], T_Result],
        nema_l1560r: typing.Callable[[], T_Result],
        nema_l2120r: typing.Callable[[], T_Result],
        nema_l2130r: typing.Callable[[], T_Result],
        nema_l2230r: typing.Callable[[], T_Result],
        cs6360c: typing.Callable[[], T_Result],
        cs6364c: typing.Callable[[], T_Result],
        cs8164c: typing.Callable[[], T_Result],
        cs8264c: typing.Callable[[], T_Result],
        cs8364c: typing.Callable[[], T_Result],
        cs8464c: typing.Callable[[], T_Result],
        ita_type_e_cee75: typing.Callable[[], T_Result],
        ita_type_f_cee73: typing.Callable[[], T_Result],
        ita_type_g_bs1363: typing.Callable[[], T_Result],
        ita_type_h: typing.Callable[[], T_Result],
        ita_type_i: typing.Callable[[], T_Result],
        ita_type_j: typing.Callable[[], T_Result],
        ita_type_k: typing.Callable[[], T_Result],
        ita_type_l_cei2350: typing.Callable[[], T_Result],
        ita_type_m_bs546: typing.Callable[[], T_Result],
        ita_type_n: typing.Callable[[], T_Result],
        ita_type_o: typing.Callable[[], T_Result],
        ita_multistandard: typing.Callable[[], T_Result],
        usb_type_a: typing.Callable[[], T_Result],
        usb_micro_b: typing.Callable[[], T_Result],
        usb_type_c: typing.Callable[[], T_Result],
        dc_terminal: typing.Callable[[], T_Result],
        hdot_cx: typing.Callable[[], T_Result],
        saf_d_grid: typing.Callable[[], T_Result],
        neutrik_power_con20a: typing.Callable[[], T_Result],
        neutrik_power_con32a: typing.Callable[[], T_Result],
        neutrik_power_con_true1: typing.Callable[[], T_Result],
        neutrik_power_con_true1top: typing.Callable[[], T_Result],
        ubiquiti_smart_power: typing.Callable[[], T_Result],
        hardwired: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PowerOutletTemplateTypeLabel.C5:
            return c5()
        if self is PowerOutletTemplateTypeLabel.C7:
            return c7()
        if self is PowerOutletTemplateTypeLabel.C13:
            return c13()
        if self is PowerOutletTemplateTypeLabel.C15:
            return c15()
        if self is PowerOutletTemplateTypeLabel.C19:
            return c19()
        if self is PowerOutletTemplateTypeLabel.C21:
            return c21()
        if self is PowerOutletTemplateTypeLabel.PNE4H:
            return pne4h()
        if self is PowerOutletTemplateTypeLabel.PNE6H:
            return pne6h()
        if self is PowerOutletTemplateTypeLabel.PNE9H:
            return pne9h()
        if self is PowerOutletTemplateTypeLabel.TWO_PE4H:
            return two_pe4h()
        if self is PowerOutletTemplateTypeLabel.TWO_PE6H:
            return two_pe6h()
        if self is PowerOutletTemplateTypeLabel.TWO_PE9H:
            return two_pe9h()
        if self is PowerOutletTemplateTypeLabel.THREE_PE4H:
            return three_pe4h()
        if self is PowerOutletTemplateTypeLabel.THREE_PE6H:
            return three_pe6h()
        if self is PowerOutletTemplateTypeLabel.THREE_PE9H:
            return three_pe9h()
        if self is PowerOutletTemplateTypeLabel.THREE_PNE4H:
            return three_pne4h()
        if self is PowerOutletTemplateTypeLabel.THREE_PNE6H:
            return three_pne6h()
        if self is PowerOutletTemplateTypeLabel.THREE_PNE9H:
            return three_pne9h()
        if self is PowerOutletTemplateTypeLabel.NEMA115R:
            return nema115r()
        if self is PowerOutletTemplateTypeLabel.NEMA515R:
            return nema515r()
        if self is PowerOutletTemplateTypeLabel.NEMA520R:
            return nema520r()
        if self is PowerOutletTemplateTypeLabel.NEMA530R:
            return nema530r()
        if self is PowerOutletTemplateTypeLabel.NEMA550R:
            return nema550r()
        if self is PowerOutletTemplateTypeLabel.NEMA615R:
            return nema615r()
        if self is PowerOutletTemplateTypeLabel.NEMA620R:
            return nema620r()
        if self is PowerOutletTemplateTypeLabel.NEMA630R:
            return nema630r()
        if self is PowerOutletTemplateTypeLabel.NEMA650R:
            return nema650r()
        if self is PowerOutletTemplateTypeLabel.NEMA1030R:
            return nema1030r()
        if self is PowerOutletTemplateTypeLabel.NEMA1050R:
            return nema1050r()
        if self is PowerOutletTemplateTypeLabel.NEMA1420R:
            return nema1420r()
        if self is PowerOutletTemplateTypeLabel.NEMA1430R:
            return nema1430r()
        if self is PowerOutletTemplateTypeLabel.NEMA1450R:
            return nema1450r()
        if self is PowerOutletTemplateTypeLabel.NEMA1460R:
            return nema1460r()
        if self is PowerOutletTemplateTypeLabel.NEMA1515R:
            return nema1515r()
        if self is PowerOutletTemplateTypeLabel.NEMA1520R:
            return nema1520r()
        if self is PowerOutletTemplateTypeLabel.NEMA1530R:
            return nema1530r()
        if self is PowerOutletTemplateTypeLabel.NEMA1550R:
            return nema1550r()
        if self is PowerOutletTemplateTypeLabel.NEMA1560R:
            return nema1560r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L115R:
            return nema_l115r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L515R:
            return nema_l515r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L520R:
            return nema_l520r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L530R:
            return nema_l530r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L550R:
            return nema_l550r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L615R:
            return nema_l615r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L620R:
            return nema_l620r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L630R:
            return nema_l630r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L650R:
            return nema_l650r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1030R:
            return nema_l1030r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1420R:
            return nema_l1420r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1430R:
            return nema_l1430r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1450R:
            return nema_l1450r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1460R:
            return nema_l1460r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1520R:
            return nema_l1520r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1530R:
            return nema_l1530r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1550R:
            return nema_l1550r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L1560R:
            return nema_l1560r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L2120R:
            return nema_l2120r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L2130R:
            return nema_l2130r()
        if self is PowerOutletTemplateTypeLabel.NEMA_L2230R:
            return nema_l2230r()
        if self is PowerOutletTemplateTypeLabel.CS6360C:
            return cs6360c()
        if self is PowerOutletTemplateTypeLabel.CS6364C:
            return cs6364c()
        if self is PowerOutletTemplateTypeLabel.CS8164C:
            return cs8164c()
        if self is PowerOutletTemplateTypeLabel.CS8264C:
            return cs8264c()
        if self is PowerOutletTemplateTypeLabel.CS8364C:
            return cs8364c()
        if self is PowerOutletTemplateTypeLabel.CS8464C:
            return cs8464c()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_E_CEE75:
            return ita_type_e_cee75()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_F_CEE73:
            return ita_type_f_cee73()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_G_BS1363:
            return ita_type_g_bs1363()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_H:
            return ita_type_h()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_I:
            return ita_type_i()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_J:
            return ita_type_j()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_K:
            return ita_type_k()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_L_CEI2350:
            return ita_type_l_cei2350()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_M_BS546:
            return ita_type_m_bs546()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_N:
            return ita_type_n()
        if self is PowerOutletTemplateTypeLabel.ITA_TYPE_O:
            return ita_type_o()
        if self is PowerOutletTemplateTypeLabel.ITA_MULTISTANDARD:
            return ita_multistandard()
        if self is PowerOutletTemplateTypeLabel.USB_TYPE_A:
            return usb_type_a()
        if self is PowerOutletTemplateTypeLabel.USB_MICRO_B:
            return usb_micro_b()
        if self is PowerOutletTemplateTypeLabel.USB_TYPE_C:
            return usb_type_c()
        if self is PowerOutletTemplateTypeLabel.DC_TERMINAL:
            return dc_terminal()
        if self is PowerOutletTemplateTypeLabel.HDOT_CX:
            return hdot_cx()
        if self is PowerOutletTemplateTypeLabel.SAF_D_GRID:
            return saf_d_grid()
        if self is PowerOutletTemplateTypeLabel.NEUTRIK_POWER_CON20A:
            return neutrik_power_con20a()
        if self is PowerOutletTemplateTypeLabel.NEUTRIK_POWER_CON32A:
            return neutrik_power_con32a()
        if self is PowerOutletTemplateTypeLabel.NEUTRIK_POWER_CON_TRUE1:
            return neutrik_power_con_true1()
        if self is PowerOutletTemplateTypeLabel.NEUTRIK_POWER_CON_TRUE1TOP:
            return neutrik_power_con_true1top()
        if self is PowerOutletTemplateTypeLabel.UBIQUITI_SMART_POWER:
            return ubiquiti_smart_power()
        if self is PowerOutletTemplateTypeLabel.HARDWIRED:
            return hardwired()
        if self is PowerOutletTemplateTypeLabel.OTHER:
            return other()

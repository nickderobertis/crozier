

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceName(enum.StrEnum):
    NNRF_NFM = "nnrf-nfm"
    NNRF_DISC = "nnrf-disc"
    NUDM_SDM = "nudm-sdm"
    NUDM_UECM = "nudm-uecm"
    NUDM_UEAU = "nudm-ueau"
    NUDM_EE = "nudm-ee"
    NUDM_PP = "nudm-pp"
    NAMF_COMM = "namf-comm"
    NAMF_EVTS = "namf-evts"
    NAMF_MT = "namf-mt"
    NAMF_LOC = "namf-loc"
    NSMF_PDUSESSION = "nsmf-pdusession"
    NSMF_EVENT_EXPOSURE = "nsmf-event-exposure"
    NAUSF_AUTH = "nausf-auth"
    NAUSF_SORPROTECTION = "nausf-sorprotection"
    NNEF_PFDMANAGEMENT = "nnef-pfdmanagement"
    NPCF_AM_POLICY_CONTROL = "npcf-am-policy-control"
    NPCF_SMPOLICYCONTROL = "npcf-smpolicycontrol"
    NPCF_POLICYAUTHORIZATION = "npcf-policyauthorization"
    NPCF_BDTPOLICYCONTROL = "npcf-bdtpolicycontrol"
    NPCF_EVENTEXPOSURE = "npcf-eventexposure"
    NPCF_UE_POLICY_CONTROL = "npcf-ue-policy-control"
    NSMSF_SMS = "nsmsf-sms"
    NNSSF_NSSELECTION = "nnssf-nsselection"
    NNSSF_NSSAIAVAILABILITY = "nnssf-nssaiavailability"
    NUDR_DR = "nudr-dr"
    NLMF_LOC = "nlmf-loc"
    N5G_EIR_EIC = "n5g-eir-eic"
    NBSF_MANAGEMENT = "nbsf-management"
    NCHF_SPENDINGLIMITCONTROL = "nchf-spendinglimitcontrol"
    NCHF_CONVERGEDCHARGING = "nchf-convergedcharging"
    NNWDAF_EVENTSSUBSCRIPTION = "nnwdaf-eventssubscription"
    NNWDAF_ANALYTICSINFO = "nnwdaf-analyticsinfo"

    def visit(
        self,
        nnrf_nfm: typing.Callable[[], T_Result],
        nnrf_disc: typing.Callable[[], T_Result],
        nudm_sdm: typing.Callable[[], T_Result],
        nudm_uecm: typing.Callable[[], T_Result],
        nudm_ueau: typing.Callable[[], T_Result],
        nudm_ee: typing.Callable[[], T_Result],
        nudm_pp: typing.Callable[[], T_Result],
        namf_comm: typing.Callable[[], T_Result],
        namf_evts: typing.Callable[[], T_Result],
        namf_mt: typing.Callable[[], T_Result],
        namf_loc: typing.Callable[[], T_Result],
        nsmf_pdusession: typing.Callable[[], T_Result],
        nsmf_event_exposure: typing.Callable[[], T_Result],
        nausf_auth: typing.Callable[[], T_Result],
        nausf_sorprotection: typing.Callable[[], T_Result],
        nnef_pfdmanagement: typing.Callable[[], T_Result],
        npcf_am_policy_control: typing.Callable[[], T_Result],
        npcf_smpolicycontrol: typing.Callable[[], T_Result],
        npcf_policyauthorization: typing.Callable[[], T_Result],
        npcf_bdtpolicycontrol: typing.Callable[[], T_Result],
        npcf_eventexposure: typing.Callable[[], T_Result],
        npcf_ue_policy_control: typing.Callable[[], T_Result],
        nsmsf_sms: typing.Callable[[], T_Result],
        nnssf_nsselection: typing.Callable[[], T_Result],
        nnssf_nssaiavailability: typing.Callable[[], T_Result],
        nudr_dr: typing.Callable[[], T_Result],
        nlmf_loc: typing.Callable[[], T_Result],
        n5g_eir_eic: typing.Callable[[], T_Result],
        nbsf_management: typing.Callable[[], T_Result],
        nchf_spendinglimitcontrol: typing.Callable[[], T_Result],
        nchf_convergedcharging: typing.Callable[[], T_Result],
        nnwdaf_eventssubscription: typing.Callable[[], T_Result],
        nnwdaf_analyticsinfo: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceName.NNRF_NFM:
            return nnrf_nfm()
        if self is ServiceName.NNRF_DISC:
            return nnrf_disc()
        if self is ServiceName.NUDM_SDM:
            return nudm_sdm()
        if self is ServiceName.NUDM_UECM:
            return nudm_uecm()
        if self is ServiceName.NUDM_UEAU:
            return nudm_ueau()
        if self is ServiceName.NUDM_EE:
            return nudm_ee()
        if self is ServiceName.NUDM_PP:
            return nudm_pp()
        if self is ServiceName.NAMF_COMM:
            return namf_comm()
        if self is ServiceName.NAMF_EVTS:
            return namf_evts()
        if self is ServiceName.NAMF_MT:
            return namf_mt()
        if self is ServiceName.NAMF_LOC:
            return namf_loc()
        if self is ServiceName.NSMF_PDUSESSION:
            return nsmf_pdusession()
        if self is ServiceName.NSMF_EVENT_EXPOSURE:
            return nsmf_event_exposure()
        if self is ServiceName.NAUSF_AUTH:
            return nausf_auth()
        if self is ServiceName.NAUSF_SORPROTECTION:
            return nausf_sorprotection()
        if self is ServiceName.NNEF_PFDMANAGEMENT:
            return nnef_pfdmanagement()
        if self is ServiceName.NPCF_AM_POLICY_CONTROL:
            return npcf_am_policy_control()
        if self is ServiceName.NPCF_SMPOLICYCONTROL:
            return npcf_smpolicycontrol()
        if self is ServiceName.NPCF_POLICYAUTHORIZATION:
            return npcf_policyauthorization()
        if self is ServiceName.NPCF_BDTPOLICYCONTROL:
            return npcf_bdtpolicycontrol()
        if self is ServiceName.NPCF_EVENTEXPOSURE:
            return npcf_eventexposure()
        if self is ServiceName.NPCF_UE_POLICY_CONTROL:
            return npcf_ue_policy_control()
        if self is ServiceName.NSMSF_SMS:
            return nsmsf_sms()
        if self is ServiceName.NNSSF_NSSELECTION:
            return nnssf_nsselection()
        if self is ServiceName.NNSSF_NSSAIAVAILABILITY:
            return nnssf_nssaiavailability()
        if self is ServiceName.NUDR_DR:
            return nudr_dr()
        if self is ServiceName.NLMF_LOC:
            return nlmf_loc()
        if self is ServiceName.N5G_EIR_EIC:
            return n5g_eir_eic()
        if self is ServiceName.NBSF_MANAGEMENT:
            return nbsf_management()
        if self is ServiceName.NCHF_SPENDINGLIMITCONTROL:
            return nchf_spendinglimitcontrol()
        if self is ServiceName.NCHF_CONVERGEDCHARGING:
            return nchf_convergedcharging()
        if self is ServiceName.NNWDAF_EVENTSSUBSCRIPTION:
            return nnwdaf_eventssubscription()
        if self is ServiceName.NNWDAF_ANALYTICSINFO:
            return nnwdaf_analyticsinfo()

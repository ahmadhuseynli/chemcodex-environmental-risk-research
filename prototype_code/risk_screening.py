"""Transparent screening calculations for the public ChemCodex research archive.

All scenario assumptions are explicit inputs. No hidden default dilution or
assessment factor is applied.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class ScreeningInputs:
    release_mass_mg: float
    receiving_volume_l: float
    dilution_factor: float
    effect_value_mg_l: float
    assessment_factor: float


@dataclass(frozen=True)
class ScreeningResult:
    pec_mg_l: float
    pnec_mg_l: float
    risk_quotient: float
    screening_flag: str

    def to_dict(self) -> dict:
        return asdict(self)


def calculate_screening_risk(inputs: ScreeningInputs) -> ScreeningResult:
    """Calculate a simple water-column screening PEC/PNEC risk quotient.

    The caller is responsible for establishing that the chosen exposure
    scenario, effect endpoint and assessment factor are appropriate.
    """
    if inputs.release_mass_mg < 0:
        raise ValueError("release_mass_mg must be non-negative")
    if inputs.receiving_volume_l <= 0:
        raise ValueError("receiving_volume_l must be > 0")
    if inputs.dilution_factor < 1:
        raise ValueError("dilution_factor must be >= 1")
    if inputs.effect_value_mg_l <= 0:
        raise ValueError("effect_value_mg_l must be > 0")
    if inputs.assessment_factor <= 0:
        raise ValueError("assessment_factor must be > 0")

    source_concentration = inputs.release_mass_mg / inputs.receiving_volume_l
    pec = source_concentration / inputs.dilution_factor
    pnec = inputs.effect_value_mg_l / inputs.assessment_factor
    rq = pec / pnec

    if rq > 1:
        flag = "screening concern - refine, mitigate or escalate"
    else:
        flag = "no exceedance at this screening tier"

    return ScreeningResult(
        pec_mg_l=pec,
        pnec_mg_l=pnec,
        risk_quotient=rq,
        screening_flag=flag,
    )

"""Small public parser derived from the project's rule-based SDS parsing branch.

This module extracts evidence. It does not assign a regulatory decision.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from typing import Iterable


H_CODE_PATTERN = re.compile(r"\bH4(?:0[0-2]|1[0-3])\b", re.IGNORECASE)

ENDPOINT_PATTERN = re.compile(
    r"""
    \b(?P<endpoint>LC50|EC50|IC50|NOEC|EC10|LL50|EL50)\b
    (?P<context>.{0,100}?)
    (?P<operator><=|>=|<|>|=|~|≈)?
    \s*
    (?P<value>\d+(?:[.,]\d+)?(?:[eE][+-]?\d+)?)
    \s*
    (?P<unit>mg/L|ug/L|µg/L|μg/L)
    """,
    re.IGNORECASE | re.VERBOSE | re.DOTALL,
)


@dataclass(frozen=True)
class AquaticEndpoint:
    endpoint: str
    value: float
    unit: str
    operator: str
    context: str

    def to_dict(self) -> dict:
        return asdict(self)


def extract_environmental_h_codes(text: str) -> list[str]:
    """Return unique environmental H400-H413 codes found in text."""
    return sorted({m.upper() for m in H_CODE_PATTERN.findall(text or "")})


def _normalise_value(value: str, unit: str) -> tuple[float, str]:
    number = float(value.replace(",", "."))
    cleaned = unit.lower().replace("μ", "µ")
    if cleaned in {"ug/l", "µg/l"}:
        return number / 1000.0, "mg/L"
    return number, "mg/L"


def extract_aquatic_endpoints(text: str) -> list[AquaticEndpoint]:
    """Extract simple aquatic endpoint/value/unit patterns from SDS text.

    This is intentionally conservative. It returns evidence candidates for
    review; it does not decide which endpoint is scientifically appropriate.
    """
    out: list[AquaticEndpoint] = []
    for match in ENDPOINT_PATTERN.finditer(text or ""):
        value, unit = _normalise_value(match.group("value"), match.group("unit"))
        context = re.sub(r"\s+", " ", match.group("context") or "").strip()
        out.append(
            AquaticEndpoint(
                endpoint=match.group("endpoint").upper(),
                value=value,
                unit=unit,
                operator=(match.group("operator") or "").strip(),
                context=context[-100:],
            )
        )
    return out


def endpoints_as_dicts(endpoints: Iterable[AquaticEndpoint]) -> list[dict]:
    return [item.to_dict() for item in endpoints]

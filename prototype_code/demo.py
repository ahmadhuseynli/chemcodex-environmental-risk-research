"""Run a synthetic ChemCodex screening example."""

import json
from pathlib import Path

from risk_screening import ScreeningInputs, calculate_screening_risk
from sds_endpoint_parser import extract_aquatic_endpoints, extract_environmental_h_codes


ROOT = Path(__file__).resolve().parents[1]
case = json.loads((ROOT / "examples" / "synthetic_case.json").read_text(encoding="utf-8"))

print("H-codes:", extract_environmental_h_codes(case["synthetic_sds_text"]))
print("Endpoints:")
for endpoint in extract_aquatic_endpoints(case["synthetic_sds_text"]):
    print(" ", endpoint.to_dict())

inputs = ScreeningInputs(**case["screening_inputs"])
result = calculate_screening_risk(inputs)

print("\nScreening result:")
print(json.dumps(result.to_dict(), indent=2))
print("\nReminder: this synthetic calculation is not a regulatory decision.")

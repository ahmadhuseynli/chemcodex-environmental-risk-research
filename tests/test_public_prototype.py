import unittest

from prototype_code.risk_screening import ScreeningInputs, calculate_screening_risk
from prototype_code.sds_endpoint_parser import (
    extract_aquatic_endpoints,
    extract_environmental_h_codes,
)


class PublicPrototypeTests(unittest.TestCase):
    def test_h_codes(self):
        self.assertEqual(
            extract_environmental_h_codes("H411 and H400; H411 repeated"),
            ["H400", "H411"],
        )

    def test_endpoint_unit_normalisation(self):
        endpoints = extract_aquatic_endpoints("Fish LC50 = 2500 ug/L")
        self.assertEqual(len(endpoints), 1)
        self.assertAlmostEqual(endpoints[0].value, 2.5)
        self.assertEqual(endpoints[0].unit, "mg/L")

    def test_rq(self):
        result = calculate_screening_risk(
            ScreeningInputs(
                release_mass_mg=500000,
                receiving_volume_l=1000000,
                dilution_factor=100,
                effect_value_mg_l=0.2,
                assessment_factor=100,
            )
        )
        self.assertAlmostEqual(result.pec_mg_l, 0.005)
        self.assertAlmostEqual(result.pnec_mg_l, 0.002)
        self.assertAlmostEqual(result.risk_quotient, 2.5)
        self.assertIn("concern", result.screening_flag)


if __name__ == "__main__":
    unittest.main()

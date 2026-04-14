import pytest
from deepeval import assert_test
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase

def test_report_faithfulness():
    # This is the "Gold Standard" output we expect
    actual_output = "Strategy Report: Competitor is $10 cheaper than our base plan."
    retrieval_context = ["Competitor AcmeCorp offers pricing at $99/mo. Our price is $109/mo."]
    
    metric = FaithfulnessMetric(threshold=0.7)
    test_case = LLMTestCase(
        input="Compare AcmeCorp pricing",
        actual_output=actual_output,
        retrieval_context=retrieval_context
    )
    
    assert_test(test_case, [metric])



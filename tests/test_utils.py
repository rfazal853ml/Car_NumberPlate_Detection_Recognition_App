import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import numpy as np
from unittest.mock import patch
from app import run_easyocr, run_paddleocr

dummy_img = np.zeros((200, 200, 3), dtype=np.uint8)

@patch("app.load_easyocr")
def test_run_easyocr(mock_easyocr):
    mock_reader = mock_easyocr.return_value
    mock_reader.readtext.return_value = [
        ((0, 0, 1, 1), "ABC123", 0.99)
    ]

    result = run_easyocr(dummy_img)
    assert result == "ABC123"


@patch("app.load_paddleocr")
def test_run_paddleocr(mock_paddleocr):
    mock_ocr = mock_paddleocr.return_value
    mock_ocr.predict.return_value = [
        {"rec_texts": ["XYZ789"]}
    ]

    result = run_paddleocr(dummy_img)
    assert result == "XYZ789"

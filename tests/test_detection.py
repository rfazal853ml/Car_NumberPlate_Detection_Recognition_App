import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import numpy as np
from unittest.mock import patch, MagicMock
from app import detect_and_ocr

dummy_img = np.zeros((200, 200, 3), dtype=np.uint8)


@patch("app.load_yolo")
@patch("app.run_easyocr")
def test_detect_and_ocr_easyocr(mock_easyocr, mock_yolo):
    mock_model = MagicMock()

    mock_result = MagicMock()
    mock_result.boxes.xyxy = [np.array([10, 10, 50, 50])]

    # 🔑 Make model callable
    mock_model.return_value = [mock_result]

    # load_yolo() returns the callable model
    mock_yolo.return_value = lambda *args, **kwargs: mock_model.return_value

    mock_easyocr.return_value = "MOCKPLATE"

    processed, crops, texts = detect_and_ocr(dummy_img, "EasyOCR")

    assert len(crops) == 1
    assert texts == ["MOCKPLATE"]
    assert processed.shape == dummy_img.shape


@patch("app.load_yolo")
@patch("app.run_paddleocr")
def test_detect_and_ocr_paddleocr(mock_paddleocr, mock_yolo):
    mock_model = MagicMock()

    mock_result = MagicMock()
    mock_result.boxes.xyxy = [np.array([20, 20, 60, 60])]

    mock_model.return_value = [mock_result]

    mock_yolo.return_value = lambda *args, **kwargs: mock_model.return_value

    mock_paddleocr.return_value = "MOCKPADDLE"

    processed, crops, texts = detect_and_ocr(dummy_img, "PaddleOCR")

    assert len(crops) == 1
    assert texts == ["MOCKPADDLE"]
    assert processed.shape == dummy_img.shape
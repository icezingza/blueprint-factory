import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import io
import pathlib
import zipfile

# Add project root to sys.path to allow importing app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock streamlit and src modules before importing app
sys.modules['streamlit'] = MagicMock()
sys.modules['src'] = MagicMock()
sys.modules['src.extractor'] = MagicMock()
sys.modules['src.packager'] = MagicMock()

from app import generate_blueprint_package

class MockUploadedFile:
    """Helper class to mock Streamlit's UploadedFile."""
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def getbuffer(self):
        return self.content

class TestBlueprintFactory(unittest.TestCase):

    def setUp(self):
        # Setup mocks for src functions
        self.mock_extract = sys.modules['src.extractor'].extract_contents
        self.mock_create_packs = sys.modules['src.packager'].create_packs

    @patch('pathlib.Path.rglob')
    def test_generate_blueprint_accuracy(self, mock_rglob):
        """
        Test Accuracy: Verifies that the function correctly orchestrates 
        extraction, packaging, and zipping (Golden Dataset approach).
        """
        # 1. Prepare Mock Input (Golden Dataset)
        input_files = [
            MockUploadedFile("doc1.pdf", b"PDF_CONTENT"),
            MockUploadedFile("text.txt", b"TXT_CONTENT")
        ]

        # 2. Mock Internal Logic Results
        # Mock extraction result
        self.mock_extract.return_value = {"doc1": "extracted_text"}
        
        # Mock packaging result (returns dict of {pack_name: path})
        mock_pack_path = pathlib.Path("/mock/path/starter")
        self.mock_create_packs.return_value = {
            "Starter": str(mock_pack_path)
        }

        # Mock file system iteration for zipping
        # Simulate finding one file inside the pack
        mock_file = MagicMock(spec=pathlib.Path)
        mock_file.relative_to.return_value = "readme.txt"
        mock_rglob.return_value = [mock_file]

        # 3. Execute Logic
        zip_buffer = generate_blueprint_package(input_files)

        # 4. Verify Results (Metrics)
        # Check if extract_contents was called
        self.assertTrue(self.mock_extract.called, "Should call extractor")
        
        # Check if create_packs was called with extracted content
        self.mock_create_packs.assert_called_with({"doc1": "extracted_text"})

        # Check if output is a valid ZIP file
        self.assertTrue(zipfile.is_zipfile(zip_buffer), "Output should be a valid ZIP file")

if __name__ == '__main__':
    unittest.main()
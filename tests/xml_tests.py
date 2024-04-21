import pytest
import logging
import xml.etree.ElementTree as ET
import services.xml_service as xml_service


class TestXMLServices:
    @pytest.fixture(autouse=True)
    def setup_logger(self, request):
        test_name = request.node.name
        self.logger = logging.getLogger(f"{__name__}.{test_name}")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] TEST LOG %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    # Test if the function correctly recognizes .xml file, case-insensitive extension.
    @pytest.mark.parametrize("file, expected_result", [("test.xml", True), ("test.XML", True), ("test.txt", False)])
    def test_is_xml_valid_file(self, file, expected_result):
        self.logger.info(f'''TEST NAME: test_is_xml_valid_file
                                EXPECTING RESULTS: {expected_result}
                                TESTING FILE: {file}''')
        result = xml_service.is_xml(f'tests/test_data/{file}')
        assert result is expected_result

    # Test if the returned root from get_root() function is in ET.Element type or is None for invalid or empty file.
    @pytest.mark.parametrize("file, expected_result",
                             [("test.xml", ET.Element), ("test.txt", type(None)), ("empty.xml", type(None))])
    def test_get_root(self, file, expected_result):
        self.logger.info(f'''TEST NAME: test_get_root_valid_xml
                                    EXPECTING RESULTS: {expected_result}
                                    TESTING FILE: {file}''')
        root = xml_service.get_root(f'tests/test_data/{file}')
        assert type(root) is expected_result, "Returned type of root was incorrect."

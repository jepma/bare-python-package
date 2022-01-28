from unittest.mock import patch

import pytest
import logging
from bare_python_package.main import main

def test_main():

    with patch("sys.argv", ["bare_python_package", "--url", "demo"]) as mock_sysargv:
        with patch("bare_python_package.main.process_url") as mock_process_url:

            main()

            mock_process_url.assert_called_once()
            assert mock_process_url.call_args.args == ('demo',)

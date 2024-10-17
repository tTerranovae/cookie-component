from unittest.mock import patch

from cookie_component import cookie_manager


def test_cookie_manager():
    cookie_name = "test_cookie"
    with patch("cookie_component.cookie_manager") as mock_cookie_manager:
        mock_storage = {}

        def side_effect(name, action, value=None):
            if action == "set":
                mock_storage[name] = value
            elif action == "get":
                return mock_storage.get(name)

        mock_cookie_manager.side_effect = side_effect
        mock_cookie_manager(cookie_name, "set", "test_value")
        cookie = mock_cookie_manager(cookie_name, "get")

        assert cookie == "test_value"

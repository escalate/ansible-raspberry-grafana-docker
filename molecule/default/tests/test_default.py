"""Role testing files using testinfra"""


def test_influxdb_service(host):
    """Check influxdb service"""
    s = host.service("grafana")
    assert s.is_running
    assert s.is_enabled

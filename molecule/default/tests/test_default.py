"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/grafana")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_data_directory(host):
    """Check data directory"""
    d = host.file("/var/lib/grafana")
    assert d.is_directory
    assert d.user == "grafana"
    assert d.group == "root"
    assert d.mode == 0o775


def test_backup_directory(host):
    """Check backup directory"""
    b = host.file("/var/backups/grafana")
    assert b.is_directory
    assert b.user == "grafana"
    assert b.group == "root"
    assert b.mode == 0o775


def test_grafana_config(host):
    """Check Grafana config file"""
    f = host.file("/etc/grafana/grafana.ini")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        "[server]\n"
        "root_url = http://localhost:3000\n"
        "\n"
        "[security]\n"
        "admin_user = admin\n"
        "admin_password = admin"
    )
    assert config in f.content_string


def test_grafana_datasources(host):
    """Check Grafana datasources file"""
    f = host.file("/etc/grafana/provisioning/datasources/datasources.yml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        "apiVersion: 1\n"
        "datasources:\n"
        "- access: proxy\n"
        "  name: Graphite\n"
        "  type: graphite\n"
    )
    assert config in f.content_string


def test_grafana_dashboards(host):
    """Check Grafana dashboards file"""
    f = host.file("/etc/grafana/provisioning/dashboards/dashboards.yml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = (
        "apiVersion: 1\n"
        "providers:\n"
        "- name: dashboards\n"
        "  options:\n"
        "    foldersFromFilesStructure: true\n"
        "    path: /etc/grafana/dashboards\n"
        "  type: file\n"
        "  updateIntervalSeconds: 30\n"
    )
    assert config in f.content_string


def test_grafana_plugins(host):
    """Check Grafana plugins"""
    f = host.file("/var/lib/grafana/plugins/grafana-piechart-panel")
    assert f.is_directory


def test_grafana_service(host):
    """Check Grafana service"""
    s = host.service("grafana")
    assert s.is_running
    assert s.is_enabled


def test_grafana_docker_container(host):
    """Check Grafana docker container"""
    d = host.docker("grafana.service").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "grafana/grafana:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "GF_LOG_LEVEL=INFO" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "grafana" in d["NetworkSettings"]["Networks"]["internal"]["Aliases"]


def test_backup_cron_job(host):
    """Check backup cron job"""
    cmd = "/usr/local/bin/backup_grafana.sh"
    f = host.file("/var/spool/cron/crontabs/root").content_string
    assert cmd in f

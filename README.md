[![Test](https://github.com/escalate/ansible-raspberry-grafana-docker/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-grafana-docker/actions/workflows/test.yml)

# Ansible Role: Raspberry - Grafana (Docker)

An Ansible role that manages [Grafana](https://grafana.com/oss/grafana/) Docker container with systemd on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-grafana-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-grafana-docker/blob/master/requirements.yml)
* Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-grafana-docker/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.grafana
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.grafana
      tags: grafana
```

## License

MIT

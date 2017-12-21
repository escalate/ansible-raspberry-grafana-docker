# Ansible Role: grafana-docker

An Ansible role that manages provision of Grafana with Docker on Raspbian and Debian OS.
This role should be compatible with OS version Stretch (9) and Jessie (8).

## Requirements

The Docker daemon should be already installed and running on the host side.
I recommend using of the Ansible Galaxy role [angstwad.docker_ubuntu](https://github.com/angstwad/docker.ubuntu) to manage the Docker daemon.

This role is tested with Ansible version greater equal 2.4.

## Install

```
$ ansible-galaxy install escalate.grafana-docker
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-grafana-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

None

## Example Playbook

```
- hosts: all
  roles:
    - escalate.grafana-docker
```

## License

MIT

# Prometheus Setup

## Overview

Prometheus is used to collect and store time-series metrics for the Smart Campus Network Monitoring System.

In this project, Prometheus collects metrics from Prometheus itself and the monitored Ubuntu system through Node Exporter.

## Components

- Prometheus
- Node Exporter
- Grafana

## Configuration

The Prometheus configuration is stored in `prometheus.yml`.

### Scrape Targets

Prometheus monitors:

1. Prometheus server
   - Target: `localhost:9090`
   - Job: `prometheus`

2. Node Exporter
   - Target: `localhost:9100`
   - Job: `node`

## Verification

Prometheus targets can be verified from:

`http://localhost:9090/targets`

Both configured targets should show the status **UP** when the services are running.

## Metrics

Node Exporter provides system-level metrics such as:

- CPU usage
- Memory usage
- Disk usage
- Network traffic
- System load
- System uptime

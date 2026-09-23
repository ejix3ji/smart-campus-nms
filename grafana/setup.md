# Grafana Setup

## Overview

Grafana is used to visualize the metrics collected by Prometheus in the Smart Campus Network Monitoring System.

## Data Source

Grafana is connected to the Prometheus server using:

`http://localhost:9090`

The Prometheus data source is used to query and display time-series metrics.

## Dashboard

The project uses the Node Exporter Full dashboard to visualize system metrics.

The dashboard provides monitoring information such as:

- CPU usage
- Memory usage
- Network traffic
- Disk usage
- System load
- System uptime

The exported dashboard configuration is stored in `dashboard.json`.

## Monitoring Flow

Node Exporter → Prometheus → Grafana

Node Exporter exposes system metrics, Prometheus collects and stores them, and Grafana provides visualization through dashboards.

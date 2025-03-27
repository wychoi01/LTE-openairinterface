# LTE-OpenAirInterface

This code is based on [`2021.w51_c`](https://gitlab.eurecom.fr/oai/openairinterface5g/-/tree/2021.w51_c?ref_type=tags).

## Features

- scheduler: **fairRR**, **subband-PF**, **radiosaber**
- filtering: **simd** + histogram
- logging: scheduler overhead, ue-side pnf packet size

## Branch

- **enb/fairRR**
- **enb/subband**
- **enb/subband-filtering**
- **enb/radiosaber**
- **enb/radiosaber-filtering**
- **ue/base**
- **ue/pnf-log** -> Commented UE failure cases for PNF packet measurement

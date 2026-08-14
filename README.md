<img width="100%" src="https://raw.githubusercontent.com/aryanputta/aryanputta/main/assets/banner.svg" />

<br/>

<div align="center">
<b>AI infrastructure · LLM inference · KV cache systems · distributed systems · cloud backends</b><br/>
<sub>Rutgers computer science and data science student. I work on inference latency, memory bandwidth, and throughput under real hardware constraints, and I contribute those fixes upstream.</sub><br/>
<sub><a href="https://aryanputta.com">portfolio</a> · <a href="https://github.com/search?q=is%3Apr+author%3Aaryanputta+is%3Amerged+archived%3Afalse&type=pullrequests">merged open-source PRs</a> · <a href="https://www.linkedin.com/in/aryanputta">LinkedIn</a></sub>
</div>

<br/><br/>

<div align="center"><b>OPEN SOURCE</b></div>

<br/>

<!-- pr-stats:start -->
<div align="center">
<sub><b>35 merged pull requests</b> across NVIDIA · IBM · Dynamo · FlashAttention · Kubernetes · Microsoft · simdutf · AWS · HuggingFace · kornia · Liger Kernel · Pulumi — inference, CUDA, CI, and ML-systems internals</sub>
</div>

<br/>

<div align="center">
<img src="https://img.shields.io/badge/NVIDIA-17_merged-111111?style=flat-square&logo=nvidia&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/IBM-3_merged-111111?style=flat-square&logo=ibm&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/Dynamo-2_merged-111111?style=flat-square&logo=nvidia&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/FlashAttention-2_merged-111111?style=flat-square&logo=pytorch&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/Kubernetes-2_merged-111111?style=flat-square&logo=kubernetes&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/Microsoft-2_merged-111111?style=flat-square&logo=microsoft&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/simdutf-2_merged-111111?style=flat-square&logo=cplusplus&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/AWS-1_merged-111111?style=flat-square&logo=amazonaws&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/HuggingFace-1_merged-111111?style=flat-square&logo=huggingface&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/kornia-1_merged-111111?style=flat-square&logo=python&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/Liger_Kernel-1_merged-111111?style=flat-square&logo=linkedin&logoColor=C9AA71" />
<img src="https://img.shields.io/badge/Pulumi-1_merged-111111?style=flat-square&logo=pulumi&logoColor=C9AA71" />
</div>
<!-- pr-stats:end -->

<br/>

<div align="center">
<table border="0" cellspacing="0" cellpadding="10">
<tr>
<td align="left" width="50%"><a href="https://github.com/NVIDIA/cuda-python/pull/2087"><code>NVIDIA/cuda-python#2087</code></a><br/><sub>FIPS-safe hashes for program cache keys</sub></td>
<td align="left" width="50%"><a href="https://github.com/NVIDIA/cuda-quantum/pull/4688"><code>NVIDIA/cuda-quantum#4688</code></a><br/><sub>nvqpp: discriminate measured-register bool iteration</sub></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/huggingface/accelerate/pull/4054"><code>huggingface/accelerate#4054</code></a><br/><sub>Aggregate profiler memory example</sub></td>
<td align="left"><a href="https://github.com/Dao-AILab/flash-attention/pull/2622"><code>Dao-AILab/flash-attention#2622</code></a><br/><sub>weights_only=True across all torch.load sites</sub></td>
</tr>
<tr>
<td align="left"><a href="https://github.com/ai-dynamo/dynamo/pull/10281"><code>ai-dynamo/dynamo#10281</code></a><br/><sub>HTTP 415 for unsupported image formats</sub></td>
<td align="left"><a href="https://github.com/linkedin/Liger-Kernel/pull/1157"><code>linkedin/Liger-Kernel#1157</code></a><br/><sub>Guard save_for_backward on grad_bias in fused linear CE</sub></td>
</tr>
</table>
</div>

<div align="center">
<sub><a href="https://github.com/search?q=is%3Apr+author%3Aaryanputta+is%3Amerged+archived%3Afalse&type=pullrequests">→ all merged pull requests</a></sub>
</div>

<br/><br/>

<div align="center"><b>SYSTEMS WORK</b></div>

<br/>

<div align="center">
<table border="0" cellspacing="0" cellpadding="14">
<tr>
<td align="left" width="50%">
<a href="https://github.com/aryanputta/KVCacheForge-X"><b><code>KVCacheForge-X</code></b></a><br/>
<sub>KV-cache bottleneck lab. Measures TTFT, latency, throughput, HBM stalls, and GPU busy against baseline deltas.</sub>
</td>
<td align="left" width="50%">
<a href="https://github.com/aryanputta/RoboFleetOps"><b><code>RoboFleetOps</code></b></a><br/>
<sub>AWS-native robotics fleet control plane on Lambda, DynamoDB, SQS, IoT Core, and API Gateway, deployed via CDK CI.</sub>
</td>
</tr>
<tr><td colspan="2" height="10"></td></tr>
<tr>
<td align="left">
<a href="https://github.com/aryanputta/PosCacheBench"><b><code>PosCacheBench</code></b></a><br/>
<sub>Long-context benchmark for positional-attention failure modes under fixed KV-cache budgets.</sub>
</td>
<td align="left">
<a href="https://github.com/aryanputta/LunarLinkBench"><b><code>LunarLinkBench</code></b></a><br/>
<sub>Monte Carlo model of lunar comms links, separating relay passes from direct-to-Earth feasibility.</sub>
</td>
</tr>
</table>
</div>

<br/><br/>

<div align="center"><b>RESEARCH</b></div>

<br/>

<div align="center">
<table border="0" cellspacing="0" cellpadding="10">
<tr>
<td align="left" width="50%">
<a href="https://aryanputta.com/assets/papers/hybrid-satellite-telemetry-anomaly-detection.pdf"><b><code>satellite telemetry anomaly detection</code></b></a><br/>
<sub>100K telemetry readings · 5 NASA/ESA fault modes · recurrence-plot CV · 0.91 F1 on Kepler-class wheel oscillation</sub><br/>
<sub><a href="https://aryanputta.com/assets/papers/hybrid-satellite-telemetry-anomaly-detection.pdf">PDF</a> · <a href="https://github.com/aryanputta/satellite-anomaly-detection">repo</a></sub>
</td>
<td align="left" width="50%">
<a href="https://aryanputta.com/assets/papers/bell-labs-innovation-ml-analysis.pdf"><b><code>bell labs ml impact analysis</code></b></a><br/>
<sub>71-paper corpus · semantic clustering · co-authorship networks · Gradient Boosting AUC 0.674 · SHAP attribution</sub><br/>
<sub><a href="https://aryanputta.com/assets/papers/bell-labs-innovation-ml-analysis.pdf">PDF</a> · <a href="https://github.com/aryanputta/belllabs-ml-impact">repo</a></sub>
</td>
</tr>
</table>
</div>

<br/><br/>

<div align="center">
<sub><b>How I work:</b> every performance claim ships with reproducible commands, a named baseline, the hardware and software environment, and an honest limitations section. A result I cannot reproduce is not a result.</sub>
</div>

<br/>

<div align="center">
<sub><b>Available for</b> software engineering, research engineering, systems engineering, and machine learning internships and co-ops, including off-cycle terms. Also AI infrastructure and ML systems roles, cloud and backend engineering, early member-of-technical-staff (MTS) programs, and founding or early-stage engineering at seed and Series A startups.</sub><br/>
<sub>Undergraduate at Rutgers University, B.S. Computer Science and Data Science, class of 2028. Based in the New York and New Jersey area, open to relocation including San Francisco and the Bay Area, and to remote.</sub><br/>
<sub><a href="https://aryanputta.com/projects">systems project evidence</a> · <a href="https://aryanputta.com/blog/kv-cache-memory-wall">KV-cache writing</a> · <a href="https://aryanputta.com">aryanputta.com</a></sub>
</div>

<br/>

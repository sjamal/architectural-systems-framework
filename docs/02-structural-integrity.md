# Module 2: Structural & Spatial Integrity

[← Back to Main Index](../README.md)

---

### 1. Dual-Justification Components
* **Architectural Reference:** Lesson 18 (*Any design decision should be justified in at least two ways*)
* **Principle:** Structural elements must perform at least two operational roles to maximize material efficiency and minimize weight.
* **IT Application:** Select components that fulfill multiple system demands concurrently to reduce operational footprint.
* **Implementation Reference:** See configuration in [`code-examples/nginx_dual_purpose.conf`](../code-examples/nginx_dual_purpose.conf) (Load Balancing + Distributed Trace Header Injection).

---

### 2. Positive and Negative Space (Solid vs. Void)
* **Architectural Reference:** Lessons 2, 3, 5, 6 (*Figure-ground theory; Designing the interstitial space*)
* **Principle:** Unbuilt spaces between structures require identical design discipline as the structures themselves.
* **IT Application:** System stability depends heavily on network boundaries, retry budgets, rate limits, and dead-letter queues between services.
* **Implementation Reference:** See Infrastructure-as-Code in [`code-examples/sqs_dead_letter_void.yaml`](../code-examples/sqs_dead_letter_void.yaml).

---

### 3. Spatial Organization
* **Architectural Reference:** Lessons 12, 13, 15 (*Ordering systems, grids, and boundaries*)
* **Principle:** Clear spatial boundaries prevent collision, reduce friction, and clarify navigation.
* **IT Application:** Enforce explicit domain boundaries through Domain-Driven Design (DDD) and isolated network subnets.

---
**Modules:** Previous: [Module 1: Foundational Vision & Intent](01-foundational-vision.md) · Next: [Module 3: Governance, Process & Evolution](03-governance-and-process.md)  
**Related docs:** [Main index](../README.md) · [Source and Scope](../README.md#source-and-scope) · [ADRs](../adrs/README.md) · [Code examples](../code-examples/README.md) · [Runbook](RUNBOOK.md)

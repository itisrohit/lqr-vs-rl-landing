# Landing under disturbance — LQR vs learned control

A rocket booster that lands itself, where the real question is what a hand-derived controller loses when the world stops matching its linear model, and what a learned policy buys back.

**Anchor paper:** [Gaudet, Linares & Furfaro, *Deep RL for Six Degree-of-Freedom Planetary Powered Descent and Landing*](https://arxiv.org/abs/1810.08719) — this project is a scoped-down, interpretable version, focused specifically on the wind-disturbance robustness question.

---

## Phases

**Phase 1 — Physics core**
- 6-DOF rigid body as a `gymnasium.Env`, Python, RK4 integrator.
- State: position, velocity, quaternion, angular velocity, fuel mass.
- Action: throttle + gimbal.
- Wind disturbance built in from the start, not bolted on later.

**Phase 2 — Classical baseline**
- Linearize near landing setpoint, derive LQR gains by hand.
- Land cleanly in calm air.
- Document exactly where/why it fails as wind increases — this failure data is a deliverable.

**Phase 3 — RL agent**
- Stable-Baselines3, PPO first.
- Train with domain randomization (wind, mass, thrust variance) — CPU/Kaggle free tier is enough.
- If HPC access holds: vectorized parallel envs + small seed/algorithm sweep (PPO vs SAC), not scale for its own sake.

**Phase 4 — Comparison**
- One clean chart set: landing success vs wind speed, fuel use, trajectory overlays at increasing disturbance.
- This is the evidence behind your pitch sentence.

**Phase 5 — Browser demo**
- Export policy to ONNX, run inference via ONNX Runtime Web.
- WebGL render, minimal HUD (altitude, velocity, fuel only).
- Optional: wind slider so a visitor can push LQR into failure and watch RL hold.

**Phase 6 — Write-up (parallel, not after)**
- Short README: what broke, why, what fixed it, with a line anchoring it against the Gaudet et al. paper.
- This is the highest-signal artifact in the whole project.

**Ships as:** repo + live browser demo + a write-up that makes the argument in one paragraph.

---

## TODOs

- [ ] Phase 1 — Physics core (gymnasium env, RK4, 6-DOF, wind disturbance)
- [ ] Phase 2 — Classical baseline (LQR, linearize near setpoint, document failure modes)
- [ ] Phase 3 — RL agent (SB3 PPO, domain randomization)
- [ ] Phase 4 — Comparison (charts: success rate, fuel, trajectory overlays)
- [ ] Phase 5 — Browser demo (ONNX export, WebGL render, wind slider)
- [ ] Phase 6 — Write-up (README, anchor against Gaudet et al.)

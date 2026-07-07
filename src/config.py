from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RocketConfig:
    mass: float
    dry_mass: float
    max_thrust: float
    isp: float
    gimbal_limit: float


@dataclass(frozen=True)
class IntegratorConfig:
    dt: float
    method: str


@dataclass(frozen=True)
class EnvConfig:
    max_steps: int
    target_altitude: float
    target_velocity: float


@dataclass(frozen=True)
class SimulatorConfig:
    rocket: RocketConfig
    integrator: IntegratorConfig
    env: EnvConfig


@dataclass(frozen=True)
class WindConfig:
    enabled: bool
    profile: str
    speed_ref: float
    altitude_ref: float
    gust_intensity: float
    direction: tuple[float, float, float]


@dataclass(frozen=True)
class LQRConfig:
    Q_position: tuple[float, float, float]
    Q_velocity: tuple[float, float, float]
    Q_attitude: tuple[float, float, float]
    Q_angular_velocity: tuple[float, float, float]
    R_throttle: float
    R_gimbal: tuple[float, float]
    hover_altitude: float


@dataclass(frozen=True)
class PPOConfig:
    n_steps: int
    batch_size: int
    n_epochs: int
    learning_rate: float
    clip_range: float
    gamma: float
    gae_lambda: float
    ent_coef: float
    vf_coef: float
    max_grad_norm: float


@dataclass(frozen=True)
class SACConfig:
    learning_rate: float
    buffer_size: int
    batch_size: int
    tau: float
    gamma: float
    ent_coef: str
    target_entropy: str
    train_freq: int
    gradient_steps: int


_ROOT = Path(__file__).resolve().parent.parent / "configs"


def _load_toml(name: str) -> dict:
    path = _ROOT / f"{name}.toml"
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_simulator() -> SimulatorConfig:
    data = _load_toml("simulator")
    return SimulatorConfig(
        rocket=RocketConfig(**data["rocket"]),
        integrator=IntegratorConfig(**data["integrator"]),
        env=EnvConfig(**data["env"]),
    )


def load_wind() -> WindConfig:
    data = _load_toml("wind")
    return WindConfig(
        enabled=data["wind"]["enabled"],
        profile=data["wind"]["profile"],
        speed_ref=data["wind"]["speed_ref"],
        altitude_ref=data["wind"]["altitude_ref"],
        gust_intensity=data["wind"]["gust_intensity"],
        direction=tuple(data["wind"]["direction"]),
    )


def load_lqr() -> LQRConfig:
    data = _load_toml("lqr")
    lqr = data["lqr"]
    ctrl = data["controller"]
    return LQRConfig(
        Q_position=tuple(lqr["Q_position"]),
        Q_velocity=tuple(lqr["Q_velocity"]),
        Q_attitude=tuple(lqr["Q_attitude"]),
        Q_angular_velocity=tuple(lqr["Q_angular_velocity"]),
        R_throttle=lqr["R_throttle"],
        R_gimbal=tuple(lqr["R_gimbal"]),
        hover_altitude=ctrl["hover_altitude"],
    )


def load_ppo() -> PPOConfig:
    data = _load_toml("ppo")
    return PPOConfig(
        n_steps=data["ppo"]["n_steps"],
        batch_size=data["ppo"]["batch_size"],
        n_epochs=data["ppo"]["n_epochs"],
        learning_rate=data["ppo"]["learning_rate"],
        clip_range=data["ppo"]["clip_range"],
        gamma=data["ppo"]["gamma"],
        gae_lambda=data["ppo"]["gae_lambda"],
        ent_coef=data["ppo"]["ent_coef"],
        vf_coef=data["ppo"]["vf_coef"],
        max_grad_norm=data["ppo"]["max_grad_norm"],
    )


def load_sac() -> SACConfig:
    data = _load_toml("sac")
    return SACConfig(
        learning_rate=data["sac"]["learning_rate"],
        buffer_size=data["sac"]["buffer_size"],
        batch_size=data["sac"]["batch_size"],
        tau=data["sac"]["tau"],
        gamma=data["sac"]["gamma"],
        ent_coef=data["sac"]["ent_coef"],
        target_entropy=data["sac"]["target_entropy"],
        train_freq=data["sac"]["train_freq"],
        gradient_steps=data["sac"]["gradient_steps"],
    )

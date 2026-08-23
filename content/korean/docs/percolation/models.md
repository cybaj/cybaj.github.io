---
title: 모델
date: 2026-08-12
tags:
- percolation
- probability
weight: 10
item: 2026-08-12-percolation
---

무엇을 무작위로 열 것인가. 퍼콜레이션의 두 기본 모델은 이 답이 다릅니다.

## 두 가지

격자 {{< katex >}}\mathbb{Z}^d{{< /katex >}} 를 생각합니다. 정수 좌표를 가진
점들이 정점(site)이고, 거리가 1인 두 정점을 잇는 선분이 간선(bond)입니다.

**결합 침투(bond percolation)** 에서는 각 간선 {{< katex >}}e{{< /katex >}} 에

{{< katex display=true >}}
\omega(e) = \begin{cases} 1 & \text{확률 } p \\ 0 & \text{확률 } 1-p \end{cases}
{{< /katex >}}

를 서로 독립으로 부여합니다. {{< katex >}}\omega(e)=1{{< /katex >}} 이면
열린 간선입니다. 사이트 침투(site percolation)에서는 같은 일을 정점에
합니다.

여기서 중요한 것은 독립성입니다. 확률 공간은 곱측도

{{< katex display=true >}}
\mathbb{P}_p = \prod_{e} \big( p\,\delta_1 + (1-p)\,\delta_0 \big)
{{< /katex >}}

이고, 이 글에서 확률이라고 하면 전부 이 측도를 가리킵니다.

## 클러스터와 침투 확률

열린 것만 따라 움직일 수 있다고 하겠습니다. 정점
{{< katex >}}x{{< /katex >}} 에서 도달 가능한 정점들의 집합이 클러스터
{{< katex >}}C(x){{< /katex >}} 입니다.

알고 싶은 것은 하나입니다. 원점의 클러스터가 무한할 확률

{{< katex display=true >}}
\theta(p) = \mathbb{P}_p\big( |C(0)| = \infty \big)
{{< /katex >}}

가 {{< katex >}}p{{< /katex >}} 에 따라 어떻게 변하는가입니다.

## 침투 확률은 증가한다

"{{< katex >}}p{{< /katex >}} 를 키우면 더 잘 뚫린다"는 당연해 보이지만,
확률을 바꾸면 확률공간 자체가 바뀌므로 그냥 비교할 수 없습니다. 한 공간 안에서
비교하도록 만들면 됩니다.

각 간선에 균등분포 {{< katex >}}U_e \sim \mathrm{Unif}[0,1]{{< /katex >}} 를 독립으로
하나씩 붙이고,

{{< katex display=true >}}
\omega_p(e) = \mathbf{1}\{ U_e < p \}
{{< /katex >}}

로 정의합니다. 각 {{< katex >}}p{{< /katex >}} 마다
{{< katex >}}\omega_p{{< /katex >}} 의 분포는 정확히
{{< katex >}}\mathbb{P}_p{{< /katex >}} 입니다. 그런데 이제 모든
{{< katex >}}p{{< /katex >}} 가 같은 {{< katex >}}U{{< /katex >}} 를 쓰므로,
{{< katex >}}p < p'{{< /katex >}} 이면 열린 간선 집합이 그대로 포함
관계가 됩니다.

{{< katex display=true >}}
\omega_p \le \omega_{p'} \quad \text{점별로}
{{< /katex >}}

무한 클러스터가 있다는 사건은 간선을 더 열어서 깨지지 않으므로
{{< katex >}}\theta(p) \le \theta(p'){{< /katex >}} 입니다. 이 논증을
결합(coupling)이라 하며, 퍼콜레이션에서 계속 쓰입니다.

## 왜 둘 다 필요한가

관을 따라 물이 흐르는 상황은 결합 침투에, 절연체에 전도성 입자가 섞인 상황은
사이트 침투에 가깝습니다.

임계값도 다릅니다. 같은 정사각 격자에서 두 모델의
{{< katex >}}p_c{{< /katex >}} 는 서로 다르며, 뒤에서 보듯 한쪽만 정확한
값이 알려져 있습니다.

---
title: 임계 확률
date: 2026-08-12
tags:
- percolation
- probability
weight: 20
item: 2026-08-12-percolation
---

{{< katex >}}p{{< /katex >}} 를 0 에서 1 까지 올린다. 무한 클러스터가 생길 확률은
어떻게 변할까.

## 0 아니면 1

무한 클러스터가 **어딘가에** 존재한다는 사건을 생각하자. 이 사건은 간선 유한
개의 상태를 바꿔도 달라지지 않는다 — 유한 개를 열거나 닫아도 무한 클러스터가
생기거나 사라지지 않기 때문이다. 즉 꼬리 사건(tail event)이고, 콜모고로프의 0-1
법칙에 따라 확률은 0 이거나 1 이다
([Percolation theory](https://en.wikipedia.org/w/index.php?oldid=1362426482)).

앞 쪽에서 {{< katex >}}\theta{{< /katex >}} 가 증가함수임을 결합으로 보였다. 둘을
합치면 결론이 나온다.

{{< katex display=true >}}
p_c = \sup\{\, p : \theta(p) = 0 \,\}
{{< /katex >}}

가 잘 정의되고, 그 아래에서는 무한 클러스터가 확률 0 으로, 위에서는 확률 1 로
존재한다. 상전이(phase transition)라는 말을 쓰는 이유가 이 이분법이다.

여기까지는 값에 대해 아무것도 말하지 않았다는 점이 중요하다. 존재만 얻었다.

## 1차원: {{< katex >}}p_c = 1{{< /katex >}}

가장 쉬운 경우부터. {{< katex >}}\mathbb{Z}{{< /katex >}} 위의 결합 침투에서
원점의 클러스터가 오른쪽으로 최소 {{< katex >}}n{{< /katex >}} 만큼 뻗으려면
{{< katex >}}n{{< /katex >}} 개의 간선이 전부 열려야 한다. 독립이므로 확률은
{{< katex >}}p^n{{< /katex >}} 이고,

{{< katex display=true >}}
\mathbb{P}_p(|C(0)| = \infty) \le \lim_{n \to \infty} 2p^n = 0
\qquad (p < 1)
{{< /katex >}}

따라서 {{< katex >}}p < 1{{< /katex >}} 이면 무한 클러스터가 없다. 1차원에서는
임계점이 끝에 있다. 뚫리려면 **모든** 간선이 열려야 하니 당연하다.

이것이 차원이 왜 중요한지를 보여준다. 2차원부터는 우회로가 생긴다.

## 2차원: {{< katex >}}p_c \ge 1/3{{< /katex >}}

우회로가 있어도 {{< katex >}}p{{< /katex >}} 가 충분히 작으면 여전히 뚫리지
않는다. 경로를 세면 보인다.

{{< katex >}}|C(0)| = \infty{{< /katex >}} 이면 원점에서 출발하는 임의로 긴
자기회피 경로(self-avoiding path)가 열려 있어야 한다. 길이
{{< katex >}}n{{< /katex >}} 인 자기회피 경로의 개수는
{{< katex >}}\mathbb{Z}^2{{< /katex >}} 에서 첫 걸음이 4 가지, 이후 되돌아가지
않으므로 많아야 3 가지씩이라

{{< katex display=true >}}
\#\{\text{길이 } n \text{ 자기회피 경로}\} \le 4 \cdot 3^{\,n-1}
{{< /katex >}}

각각이 열려 있을 확률은 {{< katex >}}p^n{{< /katex >}} 이므로, 열린 경로 개수의
기댓값은

{{< katex display=true >}}
\mathbb{E}[\#] \le 4 \cdot 3^{\,n-1} p^{\,n} = \tfrac{4}{3}(3p)^n
{{< /katex >}}

{{< katex >}}p < 1/3{{< /katex >}} 이면 {{< katex >}}3p < 1{{< /katex >}} 이므로
이 값은 0 으로 간다. 마르코프 부등식으로 확률도 0 이 되고, 따라서
{{< katex >}}\theta(p) = 0{{< /katex >}}. 결론은

{{< katex display=true >}}
p_c(\mathbb{Z}^2, \text{bond}) \ge \tfrac{1}{3}
{{< /katex >}}

한 문단으로 얻은 하한이다. 참값 {{< katex >}}1/2{{< /katex >}} 와는 거리가
있지만, {{< katex >}}p_c > 0{{< /katex >}} 임을 — 즉 상전이가 자명하지 않게
일어남을 — 증명하기에는 충분하다.

## 알려진 값

여기서부터가 이 주제의 성격을 보여준다
([Percolation threshold](https://en.wikipedia.org/w/index.php?oldid=1368848989)).

| 격자 / 모델 | {{< katex >}}p_c{{< /katex >}} | 어떻게 알려졌나 |
|---|---|---|
| {{< katex >}}\mathbb{Z}^2{{< /katex >}}, 결합 | {{< katex >}}1/2{{< /katex >}} | 증명 (Kesten, 1980) |
| {{< katex >}}\mathbb{Z}^2{{< /katex >}}, 사이트 | {{< katex >}}0.59274621 \pm 0.00000013{{< /katex >}} | 수치 시뮬레이션만 |
| 베테 격자, 차수 {{< katex >}}z{{< /katex >}} | {{< katex >}}1/(z-1){{< /katex >}} | 증명 (다음 쪽에서 유도) |
| 에르되시–레니 | {{< katex >}}1/\langle k \rangle{{< /katex >}} | 증명 (푸아송 차수분포 가정) |

{{< katex >}}\mathbb{Z}^2{{< /katex >}} 결합 침투의
{{< katex >}}1/2{{< /katex >}} 는 20년 넘게 열린 문제였다가 1980년대 초 Harry
Kesten 이 증명했다. 자기쌍대성(self-duality)으로 값이
{{< katex >}}1/2{{< /katex >}} 라는 추측은 오래전부터 있었지만, 추측과 증명
사이가 그만큼 멀었다.

사이트 침투는 사정이 다르다. **해석적으로 유도된 값이 없다.** 위 숫자는 큰
격자를 시뮬레이션해 얻은 추정치이며, 오차 범위까지 붙어 있는 것이 그 증거다.
소수점 여덟 자리를 알면서 왜 그 값인지는 모른다.

## 정리하면

대부분의 무한 격자에서 {{< katex >}}p_c{{< /katex >}} 는 정확히 계산되지 않는다.
닫힌 형태가 알려진 경우가 예외에 가깝다. 그럼에도 {{< katex >}}p_c{{< /katex >}}
가 존재하고 {{< katex >}}0 < p_c < 1{{< /katex >}} 임은 위의 두 논증으로 얻었다.

존재는 알지만 값은 모르는 상태. 퍼콜레이션 이론의 많은 부분이 그 간극에 있다.

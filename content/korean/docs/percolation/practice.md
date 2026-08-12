---
title: 어디에 쓰이는가
date: 2026-08-12
tags:
- percolation
- probability
weight: 30
item: 2026-08-12-percolation
---

격자를 떠나면 계산이 오히려 쉬워진다. 나무 구조에서는
{{< katex >}}p_c{{< /katex >}} 를 정확히 구할 수 있고, 그 방법이 네트워크로
그대로 이어진다.

## 베테 격자: 분기 과정

베테 격자는 모든 정점의 차수가 {{< katex >}}z{{< /katex >}} 인 무한 나무다.
고리가 없다는 점이 결정적이다.

원점에서 시작해 열린 간선만 따라 퍼져 나간다고 하자. 원점은 이웃이
{{< katex >}}z{{< /katex >}} 개지만, 그 다음부터는 들어온 간선 하나를 빼고
{{< katex >}}z-1{{< /katex >}} 개씩이다. 각 간선이 확률
{{< katex >}}p{{< /katex >}} 로 열리므로, 이것은 자식 수의 평균이

{{< katex display=true >}}
\mu = (z-1)\,p
{{< /katex >}}

인 분기 과정(branching process)이다.

분기 과정의 기본 정리는 이렇다. 평균 자식 수가 1 이하이면 확률 1 로 멸종하고,
1 을 넘으면 양의 확률로 영원히 산다. 직관은 단순하다.
{{< katex >}}n{{< /katex >}} 세대의 기대 개체 수가
{{< katex >}}\mu^n{{< /katex >}} 이므로, {{< katex >}}\mu < 1{{< /katex >}} 이면
기하급수적으로 0 이 된다.

무한 클러스터가 생기는 것이 곧 멸종하지 않는 것이므로

{{< katex display=true >}}
(z-1)\,p > 1 \iff p > \frac{1}{z-1}
{{< /katex >}}

즉 {{< katex >}}p_c = 1/(z-1){{< /katex >}} 이다. 고리가 없어서 각 가지가 독립인
덕분에 격자에서는 불가능했던 계산이 끝난다.

## 네트워크: 같은 논증, 다른 차수

무작위 네트워크에서도 국소적으로는 나무처럼 보이므로 같은 논증이 통한다. 다만
차수가 정점마다 다르다.

간선을 따라 도착한 정점에서 뻗어 나가는 **추가** 간선 수의 평균은
{{< katex >}}\langle k \rangle{{< /katex >}} 가 아니다. 차수가 큰 정점일수록
간선을 타고 도착할 확률이 높기 때문이다. 이 편향을 반영하면 평균 초과 차수는

{{< katex display=true >}}
\frac{\langle k^2 \rangle}{\langle k \rangle} - 1
{{< /katex >}}

이고, 여기에 {{< katex >}}p{{< /katex >}} 를 곱한 것이 분기 과정의
{{< katex >}}\mu{{< /katex >}} 다. {{< katex >}}\mu > 1{{< /katex >}} 조건에서

{{< katex display=true >}}
p_c = \frac{\langle k \rangle}{\langle k^2 \rangle - \langle k \rangle}
{{< /katex >}}

를 얻는다 ([Percolation threshold](https://en.wikipedia.org/w/index.php?oldid=1368848989)).

에르되시–레니 네트워크는 차수가 푸아송 분포를 따르고, 푸아송에서는
{{< katex >}}\langle k^2 \rangle = \langle k \rangle^2 + \langle k \rangle{{< /katex >}}
이므로

{{< katex display=true >}}
p_c = \frac{\langle k \rangle}{\langle k \rangle^2} = \frac{1}{\langle k \rangle}
{{< /katex >}}

로 간단해진다. 흔히 인용되는 {{< katex >}}1/\langle k \rangle{{< /katex >}} 는
이 특수한 경우의 결과이지 일반식이 아니다. 차수 분포의 꼬리가 두꺼워
{{< katex >}}\langle k^2 \rangle{{< /katex >}} 가 발산하면
{{< katex >}}p_c \to 0{{< /katex >}} 이 되고, 이것이 척도 없는 네트워크가 무작위
고장에 강하다고 하는 이유다.

## 재료

절연체에 전도성 입자를 섞으면 어느 농도부터 전체가 전기를 통한다. 전도도는
입자 농도에 비례해 오르지 않고 임계 농도 근처에서 급격히 바뀐다.

사이트 침투가 이 상황의 모델이다. 입자가 있는 자리가 열린 사이트다. 그리고
앞 쪽에서 봤듯 2차원 사이트 침투의 임계값은 정확히 알려져 있지 않다 — 실제
재료에서 임계 농도를 실험으로 재는 이유 중 하나다.

## 같은 이야기

세 경우 모두 형태가 같다. 무작위로 요소를 더하거나 뺀다. 연결성은 비례해서
변하지 않는다. 특정 값에서 갑자기 바뀐다.

다른 것은 그 값에 닿을 수 있는가뿐이다. 나무에서는 분기 과정으로 정확히,
격자에서는 대부분 부등식으로만, 실제 재료에서는 실험으로.

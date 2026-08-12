---
title: 구성 방정식
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 50
item: 2026-08-13-solid-mechanics
---

[보존 법칙]({{< ref "balance.md" >}}) 은 여섯 개가 모자란 채로 끝났다. 열 개의 미지수 —
{{< katex >}}\rho{{< /katex >}},
{{< katex >}}\mathbf{v}{{< /katex >}},
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} — 에 질량과 운동량이 주는 네
개의 방정식. 이 모자람은 유도의 실수가 아니다. 강철이 고무처럼 굴기를 멈추는
자리이고, 보존 원리에서 나오는 어떤 논증도 그것을 메울 수 없다.

메우는 것은 **구성 방정식**(constitutive equation)이다. 재료를 구성하는,
응력과 변형 사이의 관계다. 이 쪽은 열역학적으로 반대편에서 출발하는 둘을
유도한다. 탄성은 에너지를 저장했다가 돌려주고, 소성은 소산시키고 돌려주지
않는다.

## 구성 방정식이 가질 수 있는 형태

형태가 완전히 자유롭지는 않다. 무엇을 적기 전에 객관성이 그것을 제한하고,
그 제한은 유도해 볼 만큼 강하다.

탄성 재료의 저장 에너지가 변형 구배만의 함수
{{< katex >}}W = W(\mathbf{F}){{< /katex >}} 라 하자. 에너지는 스칼라이므로 두
관찰자가 같은 값에 동의해야 하고, [객관성]({{< ref "objectivity.md" >}}) 은
{{< katex >}}\mathbf{F}^* = \mathbf{Q}\mathbf{F}{{< /katex >}} 를 확립했다.
따라서

{{< katex display=true >}}
W(\mathbf{F}) = W(\mathbf{Q}\mathbf{F}) \qquad \text{모든 회전 } \mathbf{Q} \text{ 에 대해}
{{< /katex >}}

*모든* {{< katex >}}\mathbf{Q}{{< /katex >}} 에 대해 성립하므로 편리한 하나에
대해서도 성립한다. [운동학]({{< ref "kinematics.md" >}}) 의 극분해
{{< katex >}}\mathbf{F} = \mathbf{R}\mathbf{U}{{< /katex >}} 를 잡고
{{< katex >}}\mathbf{Q} = \mathbf{R}^T{{< /katex >}} 로 고른다.

{{< katex display=true >}}
W(\mathbf{F}) = W(\mathbf{R}^T\mathbf{R}\mathbf{U}) = W(\mathbf{U})
{{< /katex >}}

**에너지는 회전에 전혀 의존할 수 없다** — 신장에만 의존한다. 그리고
{{< katex >}}\mathbf{U} = \mathbf{C}^{1/2}{{< /katex >}} 이고 제곱근이
유일하므로, {{< katex >}}\mathbf{U}{{< /katex >}} 에 대한 의존은
{{< katex >}}\mathbf{C}{{< /katex >}}, 같은 말로
{{< katex >}}\mathbf{E}{{< /katex >}} 에 대한 의존과 같다.

{{< katex display=true >}}
W = W(\mathbf{C}) = W(\mathbf{E})
{{< /katex >}}

아홉 개였던 독립 변수가 여섯 개가 되었고, 실험이 아니라 대칭 요구에서 나왔다.
구성 법칙이 {{< katex >}}\mathbf{C}{{< /katex >}} 와
{{< katex >}}\mathbf{E}{{< /katex >}} 로 쓰이고
{{< katex >}}\mathbf{F}{{< /katex >}} 로는 결코 쓰이지 않는 이유가 이것이다 —
[응력]({{< ref "stress.md" >}}) 의 물질 좌표계 텐서들은 편리한 정도가 아니라 허용되는 유일한
인수다.

## 초탄성

응력이 저장 에너지 함수 {{< katex >}}W{{< /katex >}} — 단위 기준 부피당 변형률
에너지 밀도 — 에서 나오고 그 함수가 현재 변형에만 의존하면 그 재료는
**초탄성**(hyperelastic)이다.

정의에는 즉각적인 따름이 있다. 닫힌 변형 순환에서 한 일은 0 이다. 상태 함수에
대해 {{< katex >}}\oint \mathrm{d}W = 0{{< /katex >}} 이기 때문이다. 초탄성
재료로는 영구 기관을 만들 수 없고, 그것에 기반한 수치 기법은 몰래 에너지를
만들어 낼 수 없다. 그 안정성이 이 형식이 지배적인 실용적 이유다.

### {{< katex >}}W{{< /katex >}} 에서 {{< katex >}}\mathbf{P}{{< /katex >}}

[응력]({{< ref "stress.md" >}}) 은 단위 기준 부피당 응력 일률이
{{< katex >}}\mathbf{P}:\dot{\mathbf{F}}{{< /katex >}} 임을 확립했다. 탄성
재료에서는 그것이 전부 저장된다.

{{< katex display=true >}}
\dot{W} = \mathbf{P}:\dot{\mathbf{F}}
{{< /katex >}}

한편 {{< katex >}}W(\mathbf{F}){{< /katex >}} 에 연쇄 법칙을 쓰면

{{< katex display=true >}}
\dot{W} = \frac{\partial W}{\partial \mathbf{F}}:\dot{\mathbf{F}}
{{< /katex >}}

빼면
{{< katex >}}\big(\mathbf{P} - \partial W/\partial\mathbf{F}\big):\dot{\mathbf{F}} = 0{{< /katex >}}
이다. 변형률 속도 {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 는 임의이고 —
재료는 현재 상태에서 어느 방향으로도 변형될 수 있다 — 모든 텐서와 축약해 0 이
되는 텐서는 0 이다. 따라서

{{< katex display=true >}}
\boxed{\;\mathbf{P} = \frac{\partial W}{\partial \mathbf{F}}\;}
{{< /katex >}}

### {{< katex >}}W{{< /katex >}} 에서 {{< katex >}}\mathbf{S}{{< /katex >}}

켤레쌍 {{< katex >}}\mathbf{S}:\dot{\mathbf{E}}{{< /katex >}} 와, 객관성이
요구하는 형태 {{< katex >}}W(\mathbf{E}){{< /katex >}} 로 반복한다.

{{< katex display=true >}}
\mathbf{S}:\dot{\mathbf{E}} = \frac{\partial W}{\partial \mathbf{E}}:\dot{\mathbf{E}}
\qquad\Longrightarrow\qquad
\mathbf{S} = \frac{\partial W}{\partial \mathbf{E}}
{{< /katex >}}

{{< katex >}}\mathbf{C}{{< /katex >}} 로 바꾸려면
{{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}){{< /katex >}} 에서
성분별로
{{< katex >}}\partial\mathbf{E}/\partial\mathbf{C} = \tfrac{1}{2}{{< /katex >}}
이므로

{{< katex display=true >}}
\frac{\partial W}{\partial \mathbf{C}} = \frac{\partial W}{\partial \mathbf{E}}\cdot\frac{1}{2} = \frac{1}{2}\mathbf{S}
\qquad\Longrightarrow\qquad
\boxed{\;\mathbf{S} = 2\frac{\partial W}{\partial \mathbf{C}} = \frac{\partial W}{\partial \mathbf{E}}\;}
{{< /katex >}}

{{< katex >}}\boldsymbol{\sigma} = J^{-1}\mathbf{F}\mathbf{S}\mathbf{F}^T{{< /katex >}}
로 밀어내면 코시 응력을 얻는다.

{{< katex display=true >}}
\boxed{\;\boldsymbol{\sigma} = \frac{2}{J}\,\mathbf{F}\frac{\partial W}{\partial \mathbf{C}}\mathbf{F}^{T}\;}
{{< /katex >}}

**하나의 스칼라 함수가 역학적 응답 전체를 결정한다.** 여섯 개의 응력 성분이
숫자 하나를 미분해서 나온다. 응력이 아니라 에너지가 불변량이라는
[응력]({{< ref "stress.md" >}}) 의 관찰이 여기서 갚음을 한다.

### 생브낭-키르히호프, 숫자와 함께

가장 단순한 초탄성 모형은 선형 이론이
{{< katex >}}\boldsymbol{\varepsilon}{{< /katex >}} 를 쓰는 자리에
{{< katex >}}\mathbf{E}{{< /katex >}} 를 써서 후크 법칙을 확장한다.

{{< katex display=true >}}
W(\mathbf{E}) = \frac{\lambda}{2}\big(\operatorname{tr}\mathbf{E}\big)^2 + \mu \operatorname{tr}\big(\mathbf{E}^2\big)
{{< /katex >}}

{{< katex >}}\lambda, \mu{{< /katex >}} 는 라메 상수(Lamé constants)다.
미분하면

{{< katex display=true >}}
\mathbf{S} = \frac{\partial W}{\partial \mathbf{E}} = \lambda\big(\operatorname{tr}\mathbf{E}\big)\mathbf{I} + 2\mu\mathbf{E}
{{< /katex >}}

{{< katex >}}\lambda = 100\ \mathrm{MPa}{{< /katex >}},
{{< katex >}}\mu = 50\ \mathrm{MPa}{{< /katex >}} 로 두고
{{< katex >}}x_1{{< /katex >}} 방향으로 10% 늘이되 가로 방향은 고정한다.

{{< katex display=true >}}
\mathbf{F} = \operatorname{diag}(1.1,\, 1,\, 1), \quad J = 1.1, \quad
\mathbf{C} = \operatorname{diag}(1.21,\, 1,\, 1), \quad
\mathbf{E} = \operatorname{diag}(0.105,\, 0,\, 0)
{{< /katex >}}

{{< katex >}}\operatorname{tr}\mathbf{E} = 0.105{{< /katex >}} 이므로

{{< katex display=true >}}
\begin{aligned}
S_{11} &= (100)(0.105) + 2(50)(0.105) = 10.5 + 10.5 = 21.0\ \mathrm{MPa} \\
S_{22} = S_{33} &= (100)(0.105) + 0 = 10.5\ \mathrm{MPa}
\end{aligned}
{{< /katex >}}

가로 성분이 0 이 아닌 것은 가로 방향이 수축하지 못하게 막았기 때문이다. 그것을
붙잡고 있는 반력이다. 밀어내면

{{< katex display=true >}}
\sigma_{11} = \frac{1}{1.1}(1.1)(21.0)(1.1) = 23.1\ \mathrm{MPa},
\qquad
\sigma_{22} = \frac{1}{1.1}(1)(10.5)(1) = 9.55\ \mathrm{MPa}
{{< /katex >}}

{{< katex >}}\sigma_{11} > S_{11}{{< /katex >}} 인 것은 코시 응력이 변형된
면적을 기준으로 하기 때문이고,
{{< katex >}}\sigma_{22} < S_{22}{{< /katex >}} 인 것은 가로 면적이
{{< katex >}}x_1{{< /katex >}} 방향으로 늘어났기 때문이다. 둘 다
[응력]({{< ref "stress.md" >}}) 의 기하학적 보정이 숫자로 도착한 것이다.

이 모형에 대한 경고 하나: 가장 자연스러워 보이는 일반화이지만 **압축에서
신뢰할 수 없다**. 압축 변형률이 충분히 커지면 접선 강성이 양의 정부호를 잃고
재료가 비물리적으로 무너진다. 작거나 중간 정도의 변형률에서는 괜찮으며,
고무의 진지한 모형이라기보다 선형 이론에서 건너오는 다리로 보는 편이 맞다.

### 압축성 네오-후크

고무에 실제로 쓸 수 있는 모형이다.
{{< katex >}}I_1 = \operatorname{tr}\mathbf{C}{{< /katex >}} 로 쓰면

{{< katex display=true >}}
W = \frac{\mu}{2}\big(I_1 - 3\big) - \mu \ln J + \frac{\lambda}{2}\big(\ln J\big)^2
{{< /katex >}}

{{< katex >}}-3{{< /katex >}} 은 3차원에서의
{{< katex >}}\operatorname{tr}\mathbf{I}{{< /katex >}} 이므로 이 형태는
명시적으로 3차원용이다. 평면 문제는 3차원으로 두고 셋째 방향을 구속해야지
{{< katex >}}2\times2{{< /katex >}} 텐서로 잘라내서는 안 된다. 로그 항도 장식이
아니다. 그것이 없으면 기준 상태가 응력을 지게 된다.
{{< katex >}}\partial I_1/\partial\mathbf{C} = \mathbf{I}{{< /katex >}} 와
{{< katex >}}\partial(\ln J)/\partial\mathbf{C} = \tfrac{1}{2}\mathbf{C}^{-1}{{< /katex >}}
을 쓰면

{{< katex display=true >}}
\mathbf{S} = 2\frac{\partial W}{\partial\mathbf{C}} = \mu\big(\mathbf{I} - \mathbf{C}^{-1}\big) + \lambda\big(\ln J\big)\mathbf{C}^{-1}
{{< /katex >}}

이고, [운동학]({{< ref "kinematics.md" >}}) 의 좌 코시-그린 텐서
{{< katex >}}\mathbf{b} = \mathbf{F}\mathbf{F}^T{{< /katex >}} 로 밀어내면

{{< katex display=true >}}
\boldsymbol{\sigma} = \frac{1}{J}\Big[\mu\big(\mathbf{b} - \mathbf{I}\big) + \lambda\big(\ln J\big)\mathbf{I}\Big]
{{< /katex >}}

기준 상태를 확인한다.
{{< katex >}}\mathbf{F} = \mathbf{I}{{< /katex >}} 이면
{{< katex >}}\mathbf{b} = \mathbf{I}{{< /katex >}},
{{< katex >}}J = 1{{< /katex >}},
{{< katex >}}\ln J = 0{{< /katex >}} 이므로
{{< katex >}}\boldsymbol{\sigma} = \mathbf{0}{{< /katex >}}. 변형되지 않은
물체에는 응력이 없다. 허용되는 모형이라면 반드시 그래야 한다.

이제 숫자다. {{< katex >}}\mu = 100\ \mathrm{kPa}{{< /katex >}} 로 두고
[운동학]({{< ref "kinematics.md" >}}) 의 부피 보존 신장을 3차원으로 확장한다.

{{< katex display=true >}}
\mathbf{F} = \operatorname{diag}(2,\, 0.5,\, 1), \qquad J = 1, \qquad
\mathbf{b} = \operatorname{diag}(4,\, 0.25,\, 1)
{{< /katex >}}

{{< katex >}}\ln J = 0{{< /katex >}} 이라 체적항이 빠진다.

{{< katex display=true >}}
\boldsymbol{\sigma} = \mu\big(\mathbf{b} - \mathbf{I}\big)
= 100 \operatorname{diag}(3,\, -0.75,\, 0)
= \operatorname{diag}(300,\, -75,\, 0)\ \mathrm{kPa}
{{< /katex >}}

늘인 방향으로 인장, 누른 방향으로 압축, 건드리지 않은 방향으로는 0.
{{< katex >}}+300{{< /katex >}} 과 {{< katex >}}-75{{< /katex >}} 의 비대칭은
실재하는 비선형 효과다. 길이가 두 배가 되는 것과 절반이 되는 것은 거울상이
아니며, 선형 이론은 거울상이라고 잘못 예측한다.

## 소성

탄성은 가역적이다. 클립을 충분히 구부리면 구부러진 채로 남는다. 에너지가
저장이 아니라 재료의 재배열로 갔고 되찾을 수 없다. 소성에는 다른 기구가
필요하다. 소성 부분에는 저장 에너지 함수가 존재하지 않기 때문이다.

그것을 대신하는 재료가 셋이다.

**항복 함수.** 스칼라
{{< katex >}}f(\boldsymbol{\sigma}){{< /katex >}} 에 대해

{{< katex display=true >}}
f(\boldsymbol{\sigma}) < 0 \;\;\text{탄성}, \qquad
f(\boldsymbol{\sigma}) = 0 \;\;\text{항복 중}, \qquad
f(\boldsymbol{\sigma}) > 0 \;\;\text{허용되지 않음}
{{< /katex >}}

마지막은 모형화의 선택이 아니다. 항복 곡면 바깥의 응력 상태에는 도달할 수
없다. 거기 이르기 전에 재료가 흐르기 때문이다.

**분해.** 변형률 속도가 회복 가능한 부분과 영구적인 부분으로 나뉜다.
{{< katex >}}\mathbf{D} = \mathbf{D}^e + \mathbf{D}^p{{< /katex >}} 이고 응력은
탄성 부분만으로 결정된다.

**유동 법칙.** {{< katex >}}\mathbf{D}^p{{< /katex >}} 의 방향과 크기를 준다.
유도해야 하는 것이 이것이다.

### 최대 소산에서 나오는 유동 법칙

유도는 보존 법칙이 아니라 원리에 기댄다. 이는 분명히 말해 둘 값이 있다 —
재료 거동에 관한 가정이고, 금속에 대해서는 잘 뒷받침되며 흙과 입상 매질에서는
성립하지 않는 것으로 알려져 있다.

**최대 소성 소산 원리.** 허용되는
({{< katex >}}f(\boldsymbol{\sigma}^*) \leq 0{{< /katex >}}) 모든 응력 상태
{{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} 중에서, 주어진 소성 변형률
속도에 대해 재료가 실제로 차지하는 상태가 에너지를 가장 많이 소산시킨다.

{{< katex display=true >}}
\big(\boldsymbol{\sigma} - \boldsymbol{\sigma}^*\big) : \mathbf{D}^p \geq 0
\qquad \text{허용되는 모든 } \boldsymbol{\sigma}^* \text{ 에 대해}
{{< /katex >}}

이제 기하학으로 읽는다. 대칭 텐서의 6차원 공간에서 허용 영역
{{< katex >}}\{f \leq 0\}{{< /katex >}} 은 볼록한 물체이고
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 는 그 경계 위에 있다. 부등식은
{{< katex >}}\mathbf{D}^p{{< /katex >}} 가 그 물체의 *모든* 점
{{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} 에 대해
{{< katex >}}\boldsymbol{\sigma} - \boldsymbol{\sigma}^*{{< /katex >}} 와 둔각을
이루지 않는다는 뜻이다.

{{< katex >}}\mathbf{D}^p{{< /katex >}} 에 항복 곡면에 접하는 성분이 조금이라도
있다고 하자. 그러면 {{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} 를 곡면을
따라 그 접선 성분 방향으로 옮기면
{{< katex >}}\boldsymbol{\sigma} - \boldsymbol{\sigma}^*{{< /katex >}} 가 그것과
반대를 향하게 되어 부등식이 깨진다. 모든 선택과 양립하는 방향은 바깥 법선뿐이다.

기울기 {{< katex >}}\partial f/\partial\boldsymbol{\sigma}{{< /katex >}} 는
정의상 등위면 {{< katex >}}f = 0{{< /katex >}} 에 수직이고 바깥을 향한다.
따라서

{{< katex display=true >}}
\boxed{\;\mathbf{D}^p = \dot{\lambda}\,\frac{\partial f}{\partial \boldsymbol{\sigma}}, \qquad \dot{\lambda} \geq 0\;}
{{< /katex >}}

**관련 유동 법칙**(associated flow rule)이다. 관련이라 부르는 것은 흐름의
방향이 별도의 가정이 아니라 항복 함수 자신에 의해 정해지기 때문이다. 스칼라
{{< katex >}}\dot{\lambda}{{< /katex >}} 는 **소성 승수**(plastic multiplier)
이고 하중 조건이 정한다.

항복 곡면의 볼록성을 썼고, 그것은 부수적이지 않다. 볼록하지 않은 곡면에서는
논증이 무너지고, 오목하게 들어간 영역 안쪽의 응력 상태가 최대 소산을 어긴다.

{{< katex >}}\dot{\lambda}{{< /katex >}} 는 하중/제하 조건이 정하며, 그 조건은
카루시-쿤-터커(Karush–Kuhn–Tucker) 형태를 띤다.

{{< katex display=true >}}
\dot{\lambda} \geq 0, \qquad f \leq 0, \qquad \dot{\lambda}f = 0
{{< /katex >}}

셋째 조건이 일을 한다. 소성 흐름
({{< katex >}}\dot{\lambda} > 0{{< /katex >}})은
{{< katex >}}f = 0{{< /katex >}} 을 요구하고, 항복 곡면 안쪽
({{< katex >}}f < 0{{< /katex >}})에서는 흐름이 금지된다. 소성이 제약 최적화
문제라는 것은 비유가 아니다 — 같은 KKT 조건이며, 계산 소성학은 이를 직접
이용한다.

### 폰 미세스, 숫자와 함께

금속의 소성 흐름은 전단이 몰고 가며 정수압에는 둔감하다 — 사방에서 똑같이
눌러도 금속은 항복하지 않는다. 그래서 항복 함수는 압력을 걷어낸 부분인
**편차 응력**(deviatoric stress)으로 만든다.

{{< katex display=true >}}
p = \tfrac{1}{3}\operatorname{tr}\boldsymbol{\sigma},
\qquad
\mathbf{s} = \boldsymbol{\sigma} - p\mathbf{I},
\qquad
f(\boldsymbol{\sigma}) = \sqrt{\tfrac{3}{2}\,\mathbf{s}:\mathbf{s}} - \sigma_Y
{{< /katex >}}

{{< katex >}}\sigma_Y{{< /katex >}} 는 단축 인장에서의 항복 응력이다. 계수
{{< katex >}}\tfrac{3}{2}{{< /katex >}} 는
{{< katex >}}\sigma_{\mathrm{eq}} = \sqrt{\tfrac{3}{2}\mathbf{s}:\mathbf{s}}{{< /katex >}}
가 단축 시험에서 가한 응력과 같아지도록 고른 것이고, 아래에서 확인한다.
기울기는

{{< katex display=true >}}
\frac{\partial f}{\partial \boldsymbol{\sigma}} = \frac{3}{2\sigma_{\mathrm{eq}}}\,\mathbf{s}
{{< /katex >}}

{{< katex >}}\sigma_Y = 300\ \mathrm{MPa}{{< /katex >}} 로 두고 정확히 항복점의
단축 인장
{{< katex >}}\boldsymbol{\sigma} = \operatorname{diag}(300, 0, 0)\ \mathrm{MPa}{{< /katex >}}
를 잡는다.

{{< katex display=true >}}
p = \tfrac{1}{3}(300 + 0 + 0) = 100\ \mathrm{MPa},
\qquad
\mathbf{s} = \operatorname{diag}(200,\, -100,\, -100)\ \mathrm{MPa}
{{< /katex >}}

{{< katex display=true >}}
\sigma_{\mathrm{eq}} = \sqrt{\tfrac{3}{2}\big(200^2 + 100^2 + 100^2\big)}
= \sqrt{\tfrac{3}{2}(60000)} = \sqrt{90000} = 300\ \mathrm{MPa}
{{< /katex >}}

이므로 {{< katex >}}f = 300 - 300 = 0{{< /katex >}}. 재료는 정확히 항복점에
있고, 보정 계수 {{< katex >}}\tfrac{3}{2}{{< /katex >}} 가 확인된다 — 단축
응력 {{< katex >}}\sigma_Y{{< /katex >}} 에서 정확히 항복한다.

흐름의 방향은

{{< katex display=true >}}
\frac{\partial f}{\partial \boldsymbol{\sigma}} = \frac{3}{2(300)}\operatorname{diag}(200,\, -100,\, -100)
= \operatorname{diag}(1,\, -0.5,\, -0.5)
{{< /katex >}}

소성 승수가
{{< katex >}}\dot{\lambda} = 0.02\ \mathrm{s^{-1}}{{< /katex >}} 라면

{{< katex display=true >}}
\mathbf{D}^p = 0.02\operatorname{diag}(1,\, -0.5,\, -0.5) = \operatorname{diag}(0.02,\, -0.01,\, -0.01)\ \mathrm{s^{-1}}
{{< /katex >}}

### 숫자가 말하는 것

넣지 않은 것 둘이 떨어져 나온다.

**소성 흐름은 부피를 보존한다.** 대각합을 취한다.

{{< katex display=true >}}
\operatorname{tr}\mathbf{D}^p = 0.02 - 0.01 - 0.01 = 0
{{< /katex >}}

정확히 0 이다. 유도에서 비압축성을 부과한 곳은 없다.
{{< katex >}}f{{< /katex >}} 가 편차 응력에만 의존해서 그 기울기가 대각합 0 을
갖는 데서 따라 나왔다. 이것이 담고 있는 물리적 명제는, 금속의 소성 변형이
전위가 서로 미끄러지는 것이며 물질을 재배열할 뿐 차지하는 공간을 바꾸지
않는다는 것이다. 그 실험적 사실과 항복의 정수압 둔감성은 같은 사실이고, 유동
법칙이 하나를 다른 하나로 바꿔 준다.

**가로 수축이 정확히 늘어남의 절반이다.** 비
{{< katex >}}0.01/0.02 = 0.5{{< /katex >}} 는 소성 푸아송비
{{< katex >}}\tfrac{1}{2}{{< /katex >}} 이고 비압축성 극한이다. 같은 금속이
탄성 영역에서는 {{< katex >}}\nu \approx 0.3{{< /katex >}} 이다. 항복을 지나
당겨지는 막대는 가늘어지는 방식이 바뀌며, 그 변화는 측정된다.

## 계를 닫으며

구성 방정식이 있으면 [보존 법칙]({{< ref "balance.md" >}}) 의 셈이 닫힌다. 여섯 개의 응력
성분이 이제 변형에서 따라 나온다 — 초탄성 재료에서는
{{< katex >}}\partial W/\partial\mathbf{C}{{< /katex >}} 를 통해, 탄소성
재료에서는 하중 경로를 따라 적분한 유동 법칙을 통해. 미지수 열 개에 방정식 열
개, 그리고 경계 조건이 문제를 잘 놓인 것으로 만든다.

전체 구조는 이것이고, 한눈에 볼 값이 있다.

1. [운동학]({{< ref "kinematics.md" >}}) 이 {{< katex >}}\mathbf{F}{{< /katex >}} 로 변형을
   기술하고 회전을 {{< katex >}}\mathbf{C}{{< /katex >}} 와
   {{< katex >}}\mathbf{E}{{< /katex >}} 안에 격리한다.
2. [보존 법칙]({{< ref "balance.md" >}}) 이 보편적인 방정식을 주되 여섯 개가 모자라며,
   {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 를 대칭으로 강제한다.
3. [응력]({{< ref "stress.md" >}}) 이 세 응력 텐서가 세 좌표계에 놓인 하나의 물리량임을,
   에너지가 그 불변량임을 보인다.
4. [객관성]({{< ref "objectivity.md" >}}) 이 재료 법칙에 어떤 미분이 들어갈 수 있는지 정한다.
5. 이 쪽이 모자란 여섯을 채우고, 그것이 가질 수 있는 형태는 객관성이 미리
   지시했다.

각 단계가 다음 단계를 제약했다. 대변형 역학에 기구가 이토록 많은 이유는, 하나의
요구 — 물리는 누가 보고 있는지에 의존해서는 안 된다 — 가 일관되게 강제되기
때문이고, 그것이 거의 전부를 결정해 버리기 때문이다.

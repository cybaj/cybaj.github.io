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

[보존 법칙]({{< ref "balance.md" >}})은 방정식이 여섯 개 모자란 채로 끝났다.
미지수는 {{< katex >}}\rho{{< /katex >}},
{{< katex >}}\mathbf{v}{{< /katex >}},
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 를 합쳐 열 개인데 질량과
운동량에서 얻은 방정식은 네 개뿐이었다. 이 부족은 유도 과정의 실수가 아니다.
강철이 고무처럼 굴기를 그만두는 자리이며, 보존 원리에서 나오는 어떤 논증으로도
채울 수 없다.

채우는 것이 **구성 방정식**(constitutive equation)이다. 재료를 구성하는,
응력과 변형 사이의 관계다. 여기서는 열역학적으로 정반대편에서 출발하는 두
가지를 유도한다. 탄성은 에너지를 저장했다가 돌려주고, 소성은 흩어 버리고
돌려주지 않는다.
(개인 노트: preparation 4 : 초탄성(Hyperelasticity)과 소성(Plasticity))

## 어떤 형태까지 허용되는가

형태가 완전히 자유롭지는 않다. 무언가를 적기 전에 객관성이 먼저 제한을 걸며,
그 제한은 직접 유도해 볼 만큼 강하다.

탄성 재료의 저장 에너지가 변형 구배만의 함수
{{< katex >}}W = W(\mathbf{F}){{< /katex >}} 라고 하자. 에너지는 스칼라이므로
두 관찰자가 같은 값에 동의해야 하고,
[객관성]({{< ref "objectivity.md" >}})에서
{{< katex >}}\mathbf{F}^* = \mathbf{Q}\mathbf{F}{{< /katex >}} 임을 확인했다.
따라서

{{< katex display=true >}}
W(\mathbf{F}) = W(\mathbf{Q}\mathbf{F}) \qquad (\text{모든 회전 } \mathbf{Q} \text{ 에 대해})
{{< /katex >}}

*모든* {{< katex >}}\mathbf{Q}{{< /katex >}} 에 대해 성립하니 편한 것 하나를
골라도 된다. [운동학]({{< ref "kinematics.md" >}})의 극분해
{{< katex >}}\mathbf{F} = \mathbf{R}\mathbf{U}{{< /katex >}} 를 가져와
{{< katex >}}\mathbf{Q} = \mathbf{R}^T{{< /katex >}} 로 두면

{{< katex display=true >}}
W(\mathbf{F}) = W(\mathbf{R}^T\mathbf{R}\mathbf{U}) = W(\mathbf{U})
{{< /katex >}}

**에너지는 회전에 전혀 의존할 수 없고 오직 신장에만 의존한다.** 그리고
{{< katex >}}\mathbf{U} = \mathbf{C}^{1/2}{{< /katex >}} 이고 제곱근이
유일하므로 {{< katex >}}\mathbf{U}{{< /katex >}} 에 의존한다는 것은
{{< katex >}}\mathbf{C}{{< /katex >}}, 나아가
{{< katex >}}\mathbf{E}{{< /katex >}} 에 의존한다는 것과 같다.

{{< katex display=true >}}
W = W(\mathbf{C}) = W(\mathbf{E})
{{< /katex >}}

독립 변수가 아홉 개에서 여섯 개로 줄었고, 실험이 아니라 대칭성에 대한 요구
하나에서 나왔다. 구성 법칙을
{{< katex >}}\mathbf{C}{{< /katex >}} 나
{{< katex >}}\mathbf{E}{{< /katex >}} 로 쓰고
{{< katex >}}\mathbf{F}{{< /katex >}} 로는 절대 쓰지 않는 이유가 이것이다.
[응력]({{< ref "stress.md" >}})에 나온 기준 상태 텐서들은 단지 편리한 것이
아니라 허용되는 유일한 변수다.

## 초탄성

응력이 저장 에너지 함수 {{< katex >}}W{{< /katex >}}, 즉 단위 기준 부피당
변형률 에너지 밀도에서 나오고 그 함수가 지금의 변형에만 의존하면 그 재료를
**초탄성**(hyperelastic)이라 한다.

정의에서 바로 따라 나오는 성질이 있다. 변형을 한 바퀴 돌려 제자리로 오면 한
일이 0 이다. 상태 함수이므로
{{< katex >}}\oint \mathrm{d}W = 0{{< /katex >}} 이기 때문이다. 초탄성 재료로는
영구 기관을 만들 수 없고, 이를 바탕으로 한 수치 기법이 몰래 에너지를 만들어
내는 일도 없다. 이 안정성이 이 형식을 널리 쓰는 실질적인 이유다.

### {{< katex >}}W{{< /katex >}} 에서 {{< katex >}}\mathbf{P}{{< /katex >}} 구하기

[응력]({{< ref "stress.md" >}})에서 단위 기준 부피당 응력 일률이
{{< katex >}}\mathbf{P}:\dot{\mathbf{F}}{{< /katex >}} 임을 확인했다. 탄성
재료에서는 그것이 전부 저장된다.

{{< katex display=true >}}
\dot{W} = \mathbf{P}:\dot{\mathbf{F}}
{{< /katex >}}

한편 {{< katex >}}W(\mathbf{F}){{< /katex >}} 에 연쇄 법칙을 쓰면

{{< katex display=true >}}
\dot{W} = \frac{\partial W}{\partial \mathbf{F}}:\dot{\mathbf{F}}
{{< /katex >}}

두 식을 빼면
{{< katex >}}\big(\mathbf{P} - \partial W/\partial\mathbf{F}\big):\dot{\mathbf{F}} = 0{{< /katex >}}
이다. {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 는 임의다. 재료는 지금
상태에서 어느 방향으로든 변형될 수 있기 때문이다. 그리고 어떤 텐서와 축약해도
0 이 되는 텐서는 0 이다. 따라서

{{< katex display=true >}}
\boxed{\;\mathbf{P} = \frac{\partial W}{\partial \mathbf{F}}\;}
{{< /katex >}}

### {{< katex >}}W{{< /katex >}} 에서 {{< katex >}}\mathbf{S}{{< /katex >}} 구하기

이번에는 짝 {{< katex >}}\mathbf{S}:\dot{\mathbf{E}}{{< /katex >}} 와, 객관성이
요구하는 형태 {{< katex >}}W(\mathbf{E}){{< /katex >}} 로 같은 과정을 반복한다.

{{< katex display=true >}}
\mathbf{S}:\dot{\mathbf{E}} = \frac{\partial W}{\partial \mathbf{E}}:\dot{\mathbf{E}}
\qquad\Longrightarrow\qquad
\mathbf{S} = \frac{\partial W}{\partial \mathbf{E}}
{{< /katex >}}

{{< katex >}}\mathbf{C}{{< /katex >}} 로 바꾸려면
{{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}){{< /katex >}}
에서 성분별로
{{< katex >}}\partial\mathbf{E}/\partial\mathbf{C} = \tfrac{1}{2}{{< /katex >}}
이므로

{{< katex display=true >}}
\frac{\partial W}{\partial \mathbf{C}} = \frac{\partial W}{\partial \mathbf{E}}\cdot\frac{1}{2} = \frac{1}{2}\mathbf{S}
\qquad\Longrightarrow\qquad
\boxed{\;\mathbf{S} = 2\frac{\partial W}{\partial \mathbf{C}} = \frac{\partial W}{\partial \mathbf{E}}\;}
{{< /katex >}}

{{< katex >}}\boldsymbol{\sigma} = J^{-1}\mathbf{F}\mathbf{S}\mathbf{F}^T{{< /katex >}}
로 되돌리면 코시 응력이 나온다.

{{< katex display=true >}}
\boxed{\;\boldsymbol{\sigma} = \frac{2}{J}\,\mathbf{F}\frac{\partial W}{\partial \mathbf{C}}\mathbf{F}^{T}\;}
{{< /katex >}}

**스칼라 함수 하나가 역학적 반응 전체를 결정한다.** 응력 성분 여섯 개가 숫자
하나를 미분해서 나온다. 불변인 것은 응력이 아니라 에너지라는
[응력]({{< ref "stress.md" >}})의 관찰이 여기서 결실을 맺는다.

### 생브낭-키르히호프 모형

가장 단순한 초탄성 모형은 선형 이론이
{{< katex >}}\boldsymbol{\varepsilon}{{< /katex >}} 를 쓰던 자리에
{{< katex >}}\mathbf{E}{{< /katex >}} 를 넣어 후크 법칙을 확장한 것이다.

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
{{< katex >}}x_1{{< /katex >}} 방향으로 10% 늘이되 나머지 방향은 움직이지 못하게
잡아 둔다.

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

가로 방향 성분이 0 이 아닌 이유는 그쪽이 수축하지 못하게 막아 두었기
때문이다. 붙잡고 있는 반력인 셈이다. 되돌려 보내면

{{< katex display=true >}}
\sigma_{11} = \frac{1}{1.1}(1.1)(21.0)(1.1) = 23.1\ \mathrm{MPa},
\qquad
\sigma_{22} = \frac{1}{1.1}(1)(10.5)(1) = 9.55\ \mathrm{MPa}
{{< /katex >}}

{{< katex >}}\sigma_{11}{{< /katex >}} 이
{{< katex >}}S_{11}{{< /katex >}} 보다 큰 것은 코시 응력이 변형된 면적을 기준
삼기 때문이고,
{{< katex >}}\sigma_{22}{{< /katex >}} 가
{{< katex >}}S_{22}{{< /katex >}} 보다 작은 것은 가로 면적이
{{< katex >}}x_1{{< /katex >}} 방향으로 늘어났기 때문이다. 둘 다
[응력]({{< ref "stress.md" >}})에서 이야기한 기하학적 보정이 숫자로 나타난
것이다.

이 모형에는 주의할 점이 있다. 가장 자연스러워 보이는 확장이지만 **압축에서는
믿을 수 없다.** 압축 변형률이 어느 정도 커지면 접선 강성이 양의 정부호를 잃고
재료가 물리적으로 말이 안 되게 무너진다. 작거나 중간 정도의 변형률에서는
쓸 만하며, 고무를 제대로 다루는 모형이라기보다 선형 이론에서 넘어오는
징검다리로 보는 편이 맞다.

### 압축성 네오-후크 모형

고무에 실제로 쓸 수 있는 모형이다.
{{< katex >}}I_1 = \operatorname{tr}\mathbf{C}{{< /katex >}} 로 두면

{{< katex display=true >}}
W = \frac{\mu}{2}\big(I_1 - 3\big) - \mu \ln J + \frac{\lambda}{2}\big(\ln J\big)^2
{{< /katex >}}

여기서 {{< katex >}}-3{{< /katex >}} 은 3차원에서의
{{< katex >}}\operatorname{tr}\mathbf{I}{{< /katex >}} 이므로 이 식은 3차원
전용이다. 평면 문제라도 3차원으로 두고 세 번째 방향을 구속해야지
{{< katex >}}2\times2{{< /katex >}} 텐서로 잘라 쓰면 안 된다. 로그 항도 장식이
아니다. 그것이 없으면 변형되지 않은 상태에서도 응력이 남는다.
{{< katex >}}\partial I_1/\partial\mathbf{C} = \mathbf{I}{{< /katex >}} 와
{{< katex >}}\partial(\ln J)/\partial\mathbf{C} = \tfrac{1}{2}\mathbf{C}^{-1}{{< /katex >}}
을 쓰면

{{< katex display=true >}}
\mathbf{S} = 2\frac{\partial W}{\partial\mathbf{C}} = \mu\big(\mathbf{I} - \mathbf{C}^{-1}\big) + \lambda\big(\ln J\big)\mathbf{C}^{-1}
{{< /katex >}}

이고, [운동학]({{< ref "kinematics.md" >}})의 좌 코시-그린 텐서
{{< katex >}}\mathbf{b} = \mathbf{F}\mathbf{F}^T{{< /katex >}} 를 써서
되돌려 보내면

{{< katex display=true >}}
\boldsymbol{\sigma} = \frac{1}{J}\Big[\mu\big(\mathbf{b} - \mathbf{I}\big) + \lambda\big(\ln J\big)\mathbf{I}\Big]
{{< /katex >}}

변형되지 않은 상태를 확인해 보자.
{{< katex >}}\mathbf{F} = \mathbf{I}{{< /katex >}} 이면
{{< katex >}}\mathbf{b} = \mathbf{I}{{< /katex >}},
{{< katex >}}J = 1{{< /katex >}},
{{< katex >}}\ln J = 0{{< /katex >}} 이므로
{{< katex >}}\boldsymbol{\sigma} = \mathbf{0}{{< /katex >}} 이다. 손대지 않은
물체에는 응력이 없다. 쓸 만한 모형이라면 반드시 만족해야 하는 조건이다.

이제 숫자를 넣는다. {{< katex >}}\mu = 100\ \mathrm{kPa}{{< /katex >}} 로 두고
[운동학]({{< ref "kinematics.md" >}})에서 쓴 부피 보존 신장을 3차원으로
확장한다.

{{< katex display=true >}}
\mathbf{F} = \operatorname{diag}(2,\, 0.5,\, 1), \qquad J = 1, \qquad
\mathbf{b} = \operatorname{diag}(4,\, 0.25,\, 1)
{{< /katex >}}

{{< katex >}}\ln J = 0{{< /katex >}} 이라 부피에 관한 항은 빠진다.

{{< katex display=true >}}
\boldsymbol{\sigma} = \mu\big(\mathbf{b} - \mathbf{I}\big)
= 100 \operatorname{diag}(3,\, -0.75,\, 0)
= \operatorname{diag}(300,\, -75,\, 0)\ \mathrm{kPa}
{{< /katex >}}

늘인 방향으로는 인장, 누른 방향으로는 압축, 건드리지 않은 방향으로는 0 이다.
{{< katex >}}+300{{< /katex >}} 과 {{< katex >}}-75{{< /katex >}} 의 크기 차이는
실제로 존재하는 비선형 효과다. 길이가 두 배 되는 것과 절반 되는 것은 서로
대칭이 아니며, 선형 이론은 대칭이라고 잘못 예측한다.

## 소성

탄성은 되돌릴 수 있다. 그런데 클립을 충분히 구부리면 구부러진 채로 남는다.
에너지가 저장이 아니라 재료 내부의 재배치에 쓰였고 되찾을 수 없다. 소성에는
다른 장치가 필요하다. 소성 부분에는 저장 에너지 함수가 아예 존재하지 않기
때문이다.

그 자리를 세 가지가 대신한다.

**항복 함수.** 스칼라
{{< katex >}}f(\boldsymbol{\sigma}){{< /katex >}} 에 대해

{{< katex display=true >}}
f(\boldsymbol{\sigma}) < 0 \;\;\text{탄성}, \qquad
f(\boldsymbol{\sigma}) = 0 \;\;\text{항복 중}, \qquad
f(\boldsymbol{\sigma}) > 0 \;\;\text{불가능}
{{< /katex >}}

마지막이 모형을 세우는 사람의 선택인 것은 아니다. 항복 곡면 바깥의 응력
상태에는 애초에 도달할 수 없다. 거기 이르기 전에 재료가 흘러 버리기 때문이다.

**분해.** 변형률 속도가 되돌릴 수 있는 부분과 영구적인 부분으로 나뉜다.
{{< katex >}}\mathbf{D} = \mathbf{D}^e + \mathbf{D}^p{{< /katex >}} 이고 응력은
탄성 부분만으로 결정된다.

**유동 법칙.** {{< katex >}}\mathbf{D}^p{{< /katex >}} 가 어느 방향으로 얼마나
생기는지를 정해 준다. 유도해야 할 것이 이것이다.

### 최대 소산에서 유동 법칙 끌어내기

이 유도는 보존 법칙이 아니라 하나의 원리에 기댄다. 분명히 밝혀 둘 필요가
있는데, 재료의 거동에 관한 가정이며 금속에서는 잘 들어맞지만 흙이나 입상
매질에서는 성립하지 않는 것으로 알려져 있다.

**최대 소성 소산 원리.** 허용되는
({{< katex >}}f(\boldsymbol{\sigma}^*) \leq 0{{< /katex >}}) 모든 응력 상태
{{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} 가운데, 주어진 소성 변형률
속도에 대해 재료가 실제로 놓이는 상태가 에너지를 가장 많이 흩어 버린다.

{{< katex display=true >}}
\big(\boldsymbol{\sigma} - \boldsymbol{\sigma}^*\big) : \mathbf{D}^p \geq 0
\qquad (\text{허용되는 모든 } \boldsymbol{\sigma}^* \text{ 에 대해})
{{< /katex >}}

이제 기하학으로 읽어 보자. 대칭 텐서가 이루는 6차원 공간에서 허용 영역
{{< katex >}}\{f \leq 0\}{{< /katex >}} 는 볼록한 덩어리이고
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 는 그 경계 위에 있다. 위
부등식은 {{< katex >}}\mathbf{D}^p{{< /katex >}} 가 그 덩어리의 *어느* 점
{{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} 를 잡더라도
{{< katex >}}\boldsymbol{\sigma} - \boldsymbol{\sigma}^*{{< /katex >}} 와 둔각을
이루지 않는다는 뜻이다.

{{< katex >}}\mathbf{D}^p{{< /katex >}} 에 항복 곡면을 따라가는 성분이 조금이라도
있다고 해 보자. 그러면
{{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} 를 곡면을 따라 그 성분 쪽으로
옮겼을 때
{{< katex >}}\boldsymbol{\sigma} - \boldsymbol{\sigma}^*{{< /katex >}} 가 반대
방향을 향하게 되어 부등식이 깨진다. 모든 선택과 양립할 수 있는 방향은 곡면
바깥을 향하는 법선뿐이다.

기울기 {{< katex >}}\partial f/\partial\boldsymbol{\sigma}{{< /katex >}} 는
정의상 등위면 {{< katex >}}f = 0{{< /katex >}} 에 수직이고 바깥을 향하므로

{{< katex display=true >}}
\boxed{\;\mathbf{D}^p = \dot{\lambda}\,\frac{\partial f}{\partial \boldsymbol{\sigma}}, \qquad \dot{\lambda} \geq 0\;}
{{< /katex >}}

이를 **관련 유동 법칙**(associated flow rule)이라 한다. "관련" 이라 부르는
것은 흐르는 방향이 따로 가정한 것이 아니라 항복 함수 자체에서 정해지기
때문이다. 스칼라 {{< katex >}}\dot{\lambda}{{< /katex >}} 는 **소성
승수**(plastic multiplier)이며 하중 조건이 정한다.

논증에서 항복 곡면의 볼록성을 썼는데, 이는 부수적인 조건이 아니다. 볼록하지
않은 곡면에서는 논증이 무너지고, 안쪽으로 파인 영역에 있는 응력 상태가 최대
소산 원리를 어기게 된다.

{{< katex >}}\dot{\lambda}{{< /katex >}} 는 하중과 제하 조건이 정하며, 그
조건은 카루시-쿤-터커(Karush–Kuhn–Tucker) 형태로 쓰인다.

{{< katex display=true >}}
\dot{\lambda} \geq 0, \qquad f \leq 0, \qquad \dot{\lambda}f = 0
{{< /katex >}}

핵심은 세 번째다. 소성이 진행하려면
({{< katex >}}\dot{\lambda} > 0{{< /katex >}})
{{< katex >}}f = 0{{< /katex >}} 이어야 하고, 항복 곡면 안쪽
({{< katex >}}f < 0{{< /katex >}})에서는 흐름이 금지된다. 소성이 제약 최적화
문제라는 말은 비유가 아니다. 실제로 같은 KKT 조건이며, 계산 소성학은 이 점을
그대로 활용한다.

### 폰 미세스 항복

금속의 소성 흐름은 전단이 이끌고 정수압에는 둔감하다. 사방에서 똑같이 눌러도
금속은 항복하지 않는다. 그래서 항복 함수는 압력을 걷어낸 부분인 **편차
응력**(deviatoric stress)으로 만든다.

{{< katex display=true >}}
p = \tfrac{1}{3}\operatorname{tr}\boldsymbol{\sigma},
\qquad
\mathbf{s} = \boldsymbol{\sigma} - p\mathbf{I},
\qquad
f(\boldsymbol{\sigma}) = \sqrt{\tfrac{3}{2}\,\mathbf{s}:\mathbf{s}} - \sigma_Y
{{< /katex >}}

{{< katex >}}\sigma_Y{{< /katex >}} 는 단축 인장에서의 항복 응력이다. 앞의
{{< katex >}}\tfrac{3}{2}{{< /katex >}} 는
{{< katex >}}\sigma_{\mathrm{eq}} = \sqrt{\tfrac{3}{2}\mathbf{s}:\mathbf{s}}{{< /katex >}}
가 단축 시험에서 가한 응력과 일치하도록 맞춘 값으로, 아래에서 확인한다.
기울기는

{{< katex display=true >}}
\frac{\partial f}{\partial \boldsymbol{\sigma}} = \frac{3}{2\sigma_{\mathrm{eq}}}\,\mathbf{s}
{{< /katex >}}

{{< katex >}}\sigma_Y = 300\ \mathrm{MPa}{{< /katex >}} 로 두고 정확히 항복점에
있는 단축 인장
{{< katex >}}\boldsymbol{\sigma} = \operatorname{diag}(300, 0, 0)\ \mathrm{MPa}{{< /katex >}}
을 잡는다.

{{< katex display=true >}}
p = \tfrac{1}{3}(300 + 0 + 0) = 100\ \mathrm{MPa},
\qquad
\mathbf{s} = \operatorname{diag}(200,\, -100,\, -100)\ \mathrm{MPa}
{{< /katex >}}

{{< katex display=true >}}
\sigma_{\mathrm{eq}} = \sqrt{\tfrac{3}{2}\big(200^2 + 100^2 + 100^2\big)}
= \sqrt{\tfrac{3}{2}(60000)} = \sqrt{90000} = 300\ \mathrm{MPa}
{{< /katex >}}

이므로 {{< katex >}}f = 300 - 300 = 0{{< /katex >}} 이다. 재료가 정확히
항복점에 있고, 계수 {{< katex >}}\tfrac{3}{2}{{< /katex >}} 도 확인되었다.
단축 응력이 {{< katex >}}\sigma_Y{{< /katex >}} 에 이르면 정확히 항복한다.

흐르는 방향은

{{< katex display=true >}}
\frac{\partial f}{\partial \boldsymbol{\sigma}} = \frac{3}{2(300)}\operatorname{diag}(200,\, -100,\, -100)
= \operatorname{diag}(1,\, -0.5,\, -0.5)
{{< /katex >}}

소성 승수가
{{< katex >}}\dot{\lambda} = 0.02\ \mathrm{s^{-1}}{{< /katex >}} 라면

{{< katex display=true >}}
\mathbf{D}^p = 0.02\operatorname{diag}(1,\, -0.5,\, -0.5) = \operatorname{diag}(0.02,\, -0.01,\, -0.01)\ \mathrm{s^{-1}}
{{< /katex >}}

### 넣지 않았는데 나온 것 두 가지

**소성 변형은 부피를 바꾸지 않는다.** 대각합을 구해 보면

{{< katex display=true >}}
\operatorname{tr}\mathbf{D}^p = 0.02 - 0.01 - 0.01 = 0
{{< /katex >}}

정확히 0 이다. 유도 어디에서도 비압축성을 요구한 적이 없다.
{{< katex >}}f{{< /katex >}} 가 편차 응력에만 의존해서 그 기울기의 대각합이
0 이라는 사실에서 저절로 따라 나왔다. 이 식이 담고 있는 물리는, 금속의 소성
변형이 전위가 서로 미끄러지는 현상이어서 물질을 재배치할 뿐 차지하는 공간은
바꾸지 않는다는 것이다. 이 실험적 사실과 항복이 정수압에 둔감하다는 사실은
결국 같은 이야기이며, 유동 법칙이 하나를 다른 하나로 옮겨 준다.

**가로 수축이 정확히 늘어남의 절반이다.**
{{< katex >}}0.01/0.02 = 0.5{{< /katex >}} 는 소성 푸아송비가
{{< katex >}}\tfrac{1}{2}{{< /katex >}}, 곧 비압축성 극한이라는 뜻이다. 같은
금속이라도 탄성 영역에서는
{{< katex >}}\nu \approx 0.3{{< /katex >}} 이다. 항복점을 지나 계속 당겨지는
막대는 가늘어지는 방식 자체가 달라지며, 그 차이는 실제로 측정된다.

## 열 개의 방정식이 채워졌다

구성 방정식이 들어오면 [보존 법칙]({{< ref "balance.md" >}})에서 셌던 숫자가
맞아떨어진다. 응력 성분 여섯 개가 이제 변형에서 따라 나온다. 초탄성
재료에서는 {{< katex >}}\partial W/\partial\mathbf{C}{{< /katex >}} 를 통해,
탄소성 재료에서는 하중 경로를 따라 적분한 유동 법칙을 통해 결정된다. 미지수
열 개에 방정식 열 개, 여기에 경계 조건이 더해지면 문제가 제대로 정의된다.

전체 구조를 한눈에 정리하면 이렇다.

1. [운동학]({{< ref "kinematics.md" >}})이
   {{< katex >}}\mathbf{F}{{< /katex >}} 로 변형을 기술하고 회전을
   {{< katex >}}\mathbf{C}{{< /katex >}} 와
   {{< katex >}}\mathbf{E}{{< /katex >}} 안에 가둔다.
2. [보존 법칙]({{< ref "balance.md" >}})이 재료를 가리지 않는 방정식을 주되
   여섯 개가 모자라고, {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 가
   대칭임을 강제한다.
3. [응력]({{< ref "stress.md" >}})이 세 응력 텐서가 서로 다른 기준에서 본
   하나의 물리량임을, 그리고 변하지 않는 것은 에너지임을 보인다.
4. [객관성]({{< ref "objectivity.md" >}})이 재료 법칙에 어떤 미분을 쓸 수
   있는지를 정한다.
5. 여기서 모자란 여섯을 채우는데, 그것이 취할 수 있는 형태는 이미 객관성이
   지정해 두었다.

각 단계가 다음 단계를 제한했다. 대변형 역학에 장치가 이렇게 많은 이유는
"물리는 누가 보고 있느냐에 따라 달라지지 않는다" 는 요구 하나를 끝까지
밀어붙였기 때문이고, 그 요구가 거의 모든 것을 결정해 버리기 때문이다.

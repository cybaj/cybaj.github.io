---
title: 운동학
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 10
item: 2026-08-13-solid-mechanics
---

힘보다 변형이 먼저다. 여기서는 물체의 모양이 어떻게 바뀌는지만 다루고 왜
바뀌는지는 묻지 않는다. 이하의 결과는 물체가 강철이든 고무든 젤리든 그대로
성립한다.

## 두 개의 기준과 표기 약속

물질을 이루는 각 입자에, 아무 일도 일어나기 전에 있던 자리를 이름으로 붙인다.
기준 상태(reference configuration) {{< katex >}}\Omega_0{{< /katex >}} 에서의
위치 {{< katex >}}\mathbf{X}{{< /katex >}} 는 그 입자의 이름이지 계속 머무는
자리가 아니다. 시각 {{< katex >}}t{{< /katex >}} 에 같은 입자는

{{< katex display=true >}}
\mathbf{x} = \boldsymbol{\chi}(\mathbf{X}, t)
{{< /katex >}}

로 현재 상태(current configuration) {{< katex >}}\Omega_t{{< /katex >}} 안에
있다.

이후 모든 문서에 걸쳐 지키는 약속을 먼저 정해 둔다.

> **대문자는 기준 상태, 소문자는 현재 상태를 가리킨다.**
> {{< katex >}}\mathbf{X}{{< /katex >}} 와
> {{< katex >}}\mathbf{x}{{< /katex >}},
> {{< katex >}}\mathrm{d}V{{< /katex >}} 와
> {{< katex >}}\mathrm{d}v{{< /katex >}},
> {{< katex >}}\nabla_0{{< /katex >}}({{< katex >}}\mathbf{X}{{< /katex >}} 로
> 미분)와 {{< katex >}}\nabla{{< /katex >}}({{< katex >}}\mathbf{x}{{< /katex >}}
> 로 미분).

기술 방식도 두 가지로 나뉜다. **물질 기술**(Lagrangian description)은 양을
{{< katex >}}(\mathbf{X}, t){{< /katex >}} 의 함수로 준다. 입자 하나를 따라
가며 보는 방식이다. **공간 기술**(Eulerian description)은
{{< katex >}}(\mathbf{x}, t){{< /katex >}} 의 함수로 준다. 공간의 한 지점에
서서 그곳을 지나가는 것을 기록하는 방식이다.

고체는 대개 물질 기술을 쓴다. 기준 상태는 이미 알고 있고 현재 상태가 구하려는
답이기 때문이다. 유체는 대개 공간 기술을 쓴다. 수도꼭지에서 나오는 물이 어느
입자인지는 궁금하지 않기 때문이다.

### 물질 시간 미분

두 기술은 "변화율" 이라는 말의 뜻부터 다르고, 그 차이는 한 번 짚고 넘어가는
편이 좋다.

{{< katex >}}f(\mathbf{x}, t){{< /katex >}} 를 공간 장이라 하자. *입자가 겪는*
변화율은 그 입자의 운동을 대입한 다음 미분해서 얻는다.

{{< katex display=true >}}
\dot{f} = \frac{\mathrm{d}}{\mathrm{d}t} f\big(\boldsymbol{\chi}(\mathbf{X}, t), t\big)
= \frac{\partial f}{\partial t}\bigg|_{\mathbf{x}}
+ \frac{\partial f}{\partial x_i} \frac{\partial \chi_i}{\partial t}
= \frac{\partial f}{\partial t}\bigg|_{\mathbf{x}} + \mathbf{v} \cdot \nabla f
{{< /katex >}}

연쇄 법칙과
{{< katex >}}\mathbf{v} = \partial \boldsymbol{\chi} / \partial t{{< /katex >}}
를 썼다. 앞으로 점을 찍은 기호는 언제나 이것, 즉
{{< katex >}}\mathbf{X}{{< /katex >}} 를 고정하고 취하는 **물질 시간
미분**(material time derivative)을 뜻한다.

둘째 항 {{< katex >}}\mathbf{v} \cdot \nabla f{{< /katex >}} 는 입자가 다른
자리로 옮겨 갔다는 사실만으로 겪는 변화다. 강물은 정상 상태일 수 있다.
어디서나 {{< katex >}}\partial T / \partial t = 0{{< /katex >}} 이면서도 그
안의 물 입자는 하나같이 따뜻해질 수 있는데, 더 따뜻한 하류로 흘러가고 있기
때문이다.

## 변형 구배 텐서

물체 전체의 모양 변화는 복잡하지만, 아주 작은 영역에서의 변화는 행렬 하나로
끝난다. 가까이 있는 두 입자를 {{< katex >}}\mathbf{X}{{< /katex >}} 와
{{< katex >}}\mathbf{X} + \mathrm{d}\mathbf{X}{{< /katex >}} 에 놓는다. 변형
후의 간격은 운동을 1차까지 테일러 전개하면 나온다.

{{< katex display=true >}}
\mathrm{d}\mathbf{x} = \boldsymbol{\chi}(\mathbf{X} + \mathrm{d}\mathbf{X}, t) - \boldsymbol{\chi}(\mathbf{X}, t)
= \frac{\partial \boldsymbol{\chi}}{\partial \mathbf{X}} \, \mathrm{d}\mathbf{X} + O(|\mathrm{d}\mathbf{X}|^2)
{{< /katex >}}

여기 나타난 행렬이 **변형 구배 텐서**(deformation gradient)다.

{{< katex display=true >}}
\mathbf{F} = \frac{\partial \mathbf{x}}{\partial \mathbf{X}},
\qquad F_{iJ} = \frac{\partial x_i}{\partial X_J},
\qquad \mathrm{d}\mathbf{x} = \mathbf{F} \, \mathrm{d}\mathbf{X}
{{< /katex >}}

첨자가 소문자 {{< katex >}}i{{< /katex >}} 와 대문자
{{< katex >}}J{{< /katex >}} 로 섞여 있는 것은 그냥 멋이 아니다.
{{< katex >}}\mathbf{F}{{< /katex >}} 는 **두 점 텐서**(two-point tensor)여서
기준 상태의 벡터를 받아 현재 상태의 벡터를 내놓는다. 어느 한쪽에 속하지 않기
때문에 뒤에서 까다롭게 구는 것이다.

국소적인 변형에 관한 정보는 모두
{{< katex >}}\mathbf{F}{{< /katex >}} 안에 들어 있다. 이 문서에 나오는 다른
척도는 전부 여기서 만들어진다.

## 부피, 그리고 야코비안이 양수인 이유

기준 상태의 벡터 세 개
{{< katex >}}\mathrm{d}\mathbf{X}^{(1)}, \mathrm{d}\mathbf{X}^{(2)}, \mathrm{d}\mathbf{X}^{(3)}{{< /katex >}}
가 만드는 작은 평행육면체의 부피는
{{< katex >}}\mathrm{d}V = \mathrm{d}\mathbf{X}^{(1)} \cdot (\mathrm{d}\mathbf{X}^{(2)} \times \mathrm{d}\mathbf{X}^{(3)}){{< /katex >}}
이다. 각각은
{{< katex >}}\mathrm{d}\mathbf{x}^{(k)} = \mathbf{F} \, \mathrm{d}\mathbf{X}^{(k)}{{< /katex >}}
로 옮겨 가고, 항등식
{{< katex >}}\mathbf{Aa} \cdot (\mathbf{Ab} \times \mathbf{Ac}) = \det(\mathbf{A}) \, \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}){{< /katex >}}
에 의해

{{< katex display=true >}}
\mathrm{d}v = J \, \mathrm{d}V, \qquad J = \det \mathbf{F}
{{< /katex >}}

{{< katex >}}J{{< /katex >}} 는 **야코비안**(Jacobian), 즉 국소적인 부피비다.
{{< katex >}}J = 1{{< /katex >}} 이면 부피가 유지된다.

{{< katex >}}J{{< /katex >}} 에 붙는 제약 두 가지는 대수가 아니라 물리에서
온다. 0 이 될 수 없다. {{< katex >}}J = 0{{< /katex >}} 은 유한한 부피를
한 점으로 눌러 없애는 것이기 때문이다. 음수도 될 수 없다. 행렬식이 음수라는
것은 방향이 뒤집힌다는 뜻이고, 물체가 자기 자신을 뚫고 지나가야 한다. 따라서

{{< katex display=true >}}
J > 0 \quad \text{(언제나)}
{{< /katex >}}

이고, {{< katex >}}\mathbf{F}{{< /katex >}} 는 어디서나 역행렬을 갖는다. 이
가역성은 앞으로 계속 쓰이는데, 기술적인 편의가 아니라 물리적인 사실로
기억해 두는 편이 좋다.

### 질량과 야코비안

질량은 생기지도 사라지지도 않으므로, 물질 덩어리의 질량은 어느 기준에서 계산해도
같아야 한다.

{{< katex display=true >}}
\rho_0 \, \mathrm{d}V = \rho \, \mathrm{d}v = \rho J \, \mathrm{d}V
{{< /katex >}}

{{< katex >}}\mathrm{d}V{{< /katex >}} 가 임의이므로

{{< katex display=true >}}
\rho_0 = \rho J
{{< /katex >}}

미분이 하나도 없는, 가장 간결한 형태의 질량 보존이다.
(개인 노트: what I can do in solid mechanics' final exam)
[보존 법칙]({{< ref "balance.md" >}})에서 이것이 익숙한 편미분 방정식과 같은
내용임을 보인다.

## 변형 구배 텐서를 변형률로 쓸 수 없는 이유

변형은 전혀 주지 않고 물체를 통째로 회전만 시켜 본다. 상수 회전
{{< katex >}}\mathbf{R}{{< /katex >}} 에 대해
{{< katex >}}\mathbf{x} = \mathbf{R}\mathbf{X}{{< /katex >}} 이므로
{{< katex >}}\mathbf{F} = \mathbf{R} \neq \mathbf{I}{{< /katex >}} 이다.

변형된 것은 아무것도 없는데
{{< katex >}}\mathbf{F}{{< /katex >}} 는 변했다.
{{< katex >}}\mathbf{F} - \mathbf{I}{{< /katex >}} 를 변형률로 삼으면 그저
돌고 있을 뿐인 물체에 변형률이 있다고 말하게 되고, 그 위에 세운 재료 법칙은
회전하는 멀쩡한 막대에 응력이 생긴다고 예측할 것이다. 회전은 걸러 내야 한다.

### 극분해

거르는 방법은 정확하며, 극분해 정리(polar decomposition theorem)가 그
내용이다. {{< katex >}}J > 0{{< /katex >}} 인 모든
{{< katex >}}\mathbf{F}{{< /katex >}} 는 다음과 같이 유일하게 분해된다.

{{< katex display=true >}}
\mathbf{F} = \mathbf{R}\mathbf{U} = \mathbf{V}\mathbf{R}
{{< /katex >}}

{{< katex >}}\mathbf{R}{{< /katex >}} 은 회전이고
{{< katex >}}\mathbf{U}, \mathbf{V}{{< /katex >}} 는 대칭 양의 정부호 행렬로,
각각 **우 신장 텐서**와 **좌 신장 텐서**(right/left stretch tensor)라 한다.

증명은 짧다. {{< katex >}}\mathbf{F}^T\mathbf{F}{{< /katex >}} 는 대칭이고,
{{< katex >}}\mathbf{a} \neq \mathbf{0}{{< /katex >}} 에 대해
{{< katex >}}\mathbf{a} \cdot \mathbf{F}^T\mathbf{F}\mathbf{a} = |\mathbf{F}\mathbf{a}|^2 > 0{{< /katex >}}
이므로(다시 가역성이 쓰인다) 양의 정부호다. 대칭 양의 정부호 행렬은 대칭 양의
정부호인 제곱근을 유일하게 가지므로
{{< katex >}}\mathbf{U} = (\mathbf{F}^T\mathbf{F})^{1/2}{{< /katex >}},
{{< katex >}}\mathbf{R} = \mathbf{F}\mathbf{U}^{-1}{{< /katex >}} 로 두면

{{< katex display=true >}}
\mathbf{R}^T\mathbf{R} = \mathbf{U}^{-T}\mathbf{F}^T\mathbf{F}\mathbf{U}^{-1}
= \mathbf{U}^{-1}\mathbf{U}^2\mathbf{U}^{-1} = \mathbf{I}
{{< /katex >}}

가 되어 {{< katex >}}\mathbf{R}{{< /katex >}} 이 직교 행렬임이 확인된다.

물리적으로 말하면, 어떤 변형이든 순수한 신장 다음에 회전이거나 회전 다음에
다른 순수한 신장이다. 아주 작은 영역에서 일어날 수 있는 일은 그것뿐이다.

## 변형률 척도

분해가 알려 주는 바는 {{< katex >}}\mathbf{R}{{< /katex >}} 을 버리고
{{< katex >}}\mathbf{U}{{< /katex >}} 만 남기라는 것이다. 그런데
{{< katex >}}\mathbf{U}{{< /katex >}} 를 뽑아내려면 행렬 제곱근을 계산해야
해서 번거롭다. 그래서 대신 그 제곱을 쓴다. 이것이 **우 코시-그린
텐서**(right Cauchy–Green tensor)다.

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F} = \mathbf{U}\mathbf{R}^T\mathbf{R}\mathbf{U} = \mathbf{U}^2
{{< /katex >}}

회전이 상쇄되었고 제곱근은 쓰지 않았다.
{{< katex >}}\mathbf{C}{{< /katex >}} 는 첨자가 둘 다 대문자로, 온전히 기준
상태에 속한다.

의미는 길이 제곱의 변화다. 기준 상태의 선분
{{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}} 에 대해

{{< katex display=true >}}
|\mathrm{d}\mathbf{x}|^2 = \mathrm{d}\mathbf{x} \cdot \mathrm{d}\mathbf{x}
= \mathbf{F}\,\mathrm{d}\mathbf{X} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X}
= \mathrm{d}\mathbf{X} \cdot \mathbf{C} \, \mathrm{d}\mathbf{X}
{{< /katex >}}

{{< katex >}}\mathbf{C} = \mathbf{I}{{< /katex >}} 는 모든 선분이 길이를
유지한다는 뜻이고, 그것이 곧 "변형이 없다" 는 말이다. 이 기준선을 빼면
**그린-라그랑주 변형률 텐서**(Green–Lagrange strain tensor)가 된다.

{{< katex display=true >}}
\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}) = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I})
{{< /katex >}}

회전을 포함해 아무 변형도 없을 때 정확히
{{< katex >}}\mathbf{E} = \mathbf{0}{{< /katex >}} 이 된다. 앞의
{{< katex >}}\tfrac{1}{2}{{< /katex >}} 는 미소 변형에서 공학 변형률과 값이
맞아떨어지도록 붙인 것으로, 아래에서 확인한다.

현재 상태에도 같은 구성이 있다.
{{< katex >}}\mathbf{b} = \mathbf{F}\mathbf{F}^T = \mathbf{V}^2{{< /katex >}} 를
**좌 코시-그린 텐서**라 하며 [구성 방정식]({{< ref "constitutive.md" >}})에서
쓰인다.

### 미소 변형에서는 어떻게 되는가

변위를 {{< katex >}}\mathbf{u}{{< /katex >}} 라 하고
{{< katex >}}\mathbf{x} = \mathbf{X} + \mathbf{u}{{< /katex >}} 로 쓰면
{{< katex >}}\mathbf{F} = \mathbf{I} + \nabla_0\mathbf{u}{{< /katex >}} 이고

{{< katex display=true >}}
\mathbf{E} = \tfrac{1}{2}\big[(\mathbf{I} + \nabla_0\mathbf{u})^T(\mathbf{I} + \nabla_0\mathbf{u}) - \mathbf{I}\big]
= \tfrac{1}{2}\big(\nabla_0\mathbf{u} + \nabla_0\mathbf{u}^T\big) + \tfrac{1}{2}\nabla_0\mathbf{u}^T\nabla_0\mathbf{u}
{{< /katex >}}

변위 기울기가 작으면 2차항은 1차항에 비해 무시할 수 있고, 익숙한 공학
변형률만 남는다.

{{< katex display=true >}}
\boldsymbol{\varepsilon} = \tfrac{1}{2}\big(\nabla_0\mathbf{u} + \nabla_0\mathbf{u}^T\big)
{{< /katex >}}

학부에서 배우는 탄성론은 이 식을 선형화한 것이다. 그리고 방금 버린 2차항이야말로
선형 이론을 무리하게 밀어붙였을 때 회전을 변형률로 착각하게 만드는 항이다.

## 변화율: 속도 구배, 변형률 속도, 스핀

이후 내용에는 변형뿐 아니라 변형의 속도가 필요하다. 공간 속도장을 공간으로
미분해 **속도 구배 텐서**(velocity gradient)를 정의한다.

{{< katex display=true >}}
\mathbf{L} = \frac{\partial \mathbf{v}}{\partial \mathbf{x}}, \qquad L_{ij} = \frac{\partial v_i}{\partial x_j}
{{< /katex >}}

{{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 와의 관계는 편미분의 순서를 바꾸면
바로 나온다.

{{< katex display=true >}}
\dot{\mathbf{F}} = \frac{\partial}{\partial t}\frac{\partial \mathbf{x}}{\partial \mathbf{X}}
= \frac{\partial \mathbf{v}}{\partial \mathbf{X}}
= \frac{\partial \mathbf{v}}{\partial \mathbf{x}} \frac{\partial \mathbf{x}}{\partial \mathbf{X}}
= \mathbf{L}\mathbf{F}
\qquad \Longrightarrow \qquad
\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}
{{< /katex >}}

이것을 대칭 부분과 반대칭 부분으로 나눈다.

{{< katex display=true >}}
\mathbf{D} = \tfrac{1}{2}(\mathbf{L} + \mathbf{L}^T), \qquad
\mathbf{W} = \tfrac{1}{2}(\mathbf{L} - \mathbf{L}^T), \qquad
\mathbf{L} = \mathbf{D} + \mathbf{W}
{{< /katex >}}

{{< katex >}}\mathbf{D}{{< /katex >}} 를 **변형률 속도**(rate of deformation),
{{< katex >}}\mathbf{W}{{< /katex >}} 를 **스핀**(spin)이라 한다. 물체가
통째로 회전할 때 {{< katex >}}\mathbf{D}{{< /katex >}} 는 사라지고
{{< katex >}}\mathbf{W}{{< /katex >}} 는 남는다. 변형을 담당하는 쪽이
{{< katex >}}\mathbf{D}{{< /katex >}}, 회전을 담당하는 쪽이
{{< katex >}}\mathbf{W}{{< /katex >}} 인 것이다.
[응력]({{< ref "stress.md" >}})에서는 이 분해가 곧 회전에는 에너지가 들지
않는다는 결론으로 이어진다.

### 야코비안의 변화율

[보존 법칙]({{< ref "balance.md" >}})에서 쓸 항등식이 하나 더 있다. 행렬식의
미분에 관한 야코비 공식으로부터

{{< katex display=true >}}
\dot{J} = \frac{\mathrm{d}}{\mathrm{d}t}\det\mathbf{F}
= \det\mathbf{F} \, \operatorname{tr}\!\big(\mathbf{F}^{-1}\dot{\mathbf{F}}\big)
= J \operatorname{tr}\!\big(\dot{\mathbf{F}}\mathbf{F}^{-1}\big)
= J \operatorname{tr}\mathbf{L}
= J \, \nabla \cdot \mathbf{v}
{{< /katex >}}

세 번째 등호에서 대각합의 순환 성질을 썼다. 뜻은 분명하다. 부피는 속도의
발산만큼의 비율로 늘어나며, 비압축성 운동이란
{{< katex >}}\nabla \cdot \mathbf{v} = 0{{< /katex >}} 인 운동이다.

## 숫자로 확인하기

한 변의 길이가 1인 고무판을 가로로 두 배 늘이고 세로로 절반으로 누른다.
대응 관계는 {{< katex >}}x_1 = 2X_1{{< /katex >}},
{{< katex >}}x_2 = 0.5 X_2{{< /katex >}} 이므로
(개인 노트: basic concepts on solid mechanics' final exam)

{{< katex display=true >}}
\mathbf{F} = \begin{bmatrix} 2 & 0 \\ 0 & 0.5 \end{bmatrix},
\qquad J = \det\mathbf{F} = 2 \times 0.5 = 1
{{< /katex >}}

넓이는 그대로다. 이어서

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F} = \begin{bmatrix} 4 & 0 \\ 0 & 0.25 \end{bmatrix},
\qquad
\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}) = \begin{bmatrix} 1.5 & 0 \\ 0 & -0.375 \end{bmatrix}
{{< /katex >}}

{{< katex >}}\mathbf{C}{{< /katex >}} 의 대각 성분은 신장률의 제곱
({{< katex >}}2^2 = 4{{< /katex >}},
{{< katex >}}0.5^2 = 0.25{{< /katex >}})이고,
{{< katex >}}\mathbf{E}{{< /katex >}} 는
{{< katex >}}x_1{{< /katex >}} 방향으로 늘어나고
{{< katex >}}x_2{{< /katex >}} 방향으로 줄어들었음을 말해 준다. 다만
{{< katex >}}\mathbf{E}{{< /katex >}} 는 공학 변형률
{{< katex >}}\operatorname{diag}(1.0, -0.5){{< /katex >}} 와 다르다. 100%
신장에서는 앞서 버렸던 2차항이 1차항과 같은 크기가 되어 두 척도가 갈라지기
때문이다. 이 구별이 말장난이 아니게 되는 영역이 바로 여기다.

### 회전을 넣어 보면

이제 이 모든 구성의 출발점이었던 경우다. 변형 없이
{{< katex >}}90^\circ{{< /katex >}} 회전만 준다.

{{< katex display=true >}}
\mathbf{F} = \mathbf{R} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex >}}J = 0 \cdot 0 - (-1)(1) = 1{{< /katex >}} 이고

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F}
= \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \mathbf{I}
{{< /katex >}}

따라서 {{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{I} - \mathbf{I}) = \mathbf{0}{{< /katex >}}
이다.

근사적으로 0 에 가까운 것이 아니라 정확히 0 이다. 반면
{{< katex >}}\mathbf{F} - \mathbf{I}{{< /katex >}} 의 성분은 크기가 1 이나
된다. 어설픈 변형률 척도였다면 손도 대지 않은 물체에 100% 변형률이 있다고
보고했을 것이다. 그것을 없애 준 것이
{{< katex >}}\mathbf{F}^T\mathbf{F}{{< /katex >}} 의 전치다.

모양 변화를 기술했고 회전도 따로 떼어 놓았으니, 이제
[보존 법칙]({{< ref "balance.md" >}})에서 힘을 다룰 수 있다.

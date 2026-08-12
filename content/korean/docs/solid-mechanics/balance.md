---
title: 보존 법칙
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 20
item: 2026-08-13-solid-mechanics
---

네 개의 명제, 어느 것도 특정 재료에 관한 것이 아니다. 질량은 보존되고,
선운동량이 평형을 이루고, 각운동량이 평형을 이루고, 에너지가 보존된다. 강철도
고무도 물도 넷을 똑같이 따른다. 그것들을 가르는 모든 것은
[구성 방정식]({{< ref "constitutive.md" >}}) 까지 기다린다.

각 법칙은 유한한 물질 덩어리에 대한 명제로 시작해서 모든 점에서 성립하는
편미분 방정식으로 끝난다. 그 변환을 매번 해내는 도구가 같으므로 그것부터
본다.

## 두 개의 도구

### 레이놀즈 수송 정리

보존 법칙은 *물질* 영역이 나르는 양의 변화율에 관해 말한다. 물질 영역이란
언제나 같은 입자들을 담는 영역이고, 따라서 그 경계는 움직인다. 움직이는
영역 위의 적분을 미분하는 일은 간단하지 않다. 피적분 함수와 적분 영역이 모두
시간에 의존하기 때문이다.

요령은 고정된 영역으로 바꾸는 것이다. 임의의 공간 장
{{< katex >}}\phi(\mathbf{x}, t){{< /katex >}} 에 대해
{{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}} 를 써서 적분을
움직이지 않는 기준 상태로 당겨온다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \phi \, \mathrm{d}v
= \frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_0} \phi J \, \mathrm{d}V
= \int_{\Omega_0} \frac{\mathrm{d}}{\mathrm{d}t}(\phi J) \, \mathrm{d}V
{{< /katex >}}

미분과 적분을 바꿔도 되는 이유는 {{< katex >}}\Omega_0{{< /katex >}} 가 시간에
대해 고정되어 있기 때문이다. 곱의 미분법으로 전개하고
[운동학]({{< ref "kinematics.md" >}}) 의
{{< katex >}}\dot{J} = J \nabla \cdot \mathbf{v}{{< /katex >}} 를 대입한다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}(\phi J) = \dot{\phi} J + \phi \dot{J}
= J\big(\dot{\phi} + \phi \, \nabla \cdot \mathbf{v}\big)
{{< /katex >}}

{{< katex >}}J \, \mathrm{d}V = \mathrm{d}v{{< /katex >}} 로 다시 밀어낸다.

{{< katex display=true >}}
\boxed{\;\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \phi \, \mathrm{d}v
= \int_{\Omega_t} \big(\dot{\phi} + \phi \, \nabla \cdot \mathbf{v}\big) \, \mathrm{d}v\;}
{{< /katex >}}

**레이놀즈 수송 정리**(Reynolds transport theorem)다. 첫 항은 양 자체의
변화이고, 둘째 항은 영역이 커지거나 작아져서 생기는 변화다.

### 국소화

아래의 모든 유도는
{{< katex >}}\int_{\Omega_t} (\cdots) \, \mathrm{d}v = 0{{< /katex >}} 꼴에
이르러 피적분 함수가 점마다 0 이라고 결론짓는다. 이 단계의 근거는 한 번
적어 둘 값이 있다.

적분이 0 인 것은 *모든* 물질 영역에 대해서지 특정 영역에 대해서가 아니다.
보존 법칙이 애초에 특정 덩어리에 관한 것이 아니었기 때문이다. 어떤 점
{{< katex >}}\mathbf{x}_0{{< /katex >}} 에서 피적분 함수가 양수라고 하자.
연속성에 의해 {{< katex >}}\mathbf{x}_0{{< /katex >}} 주위의 어떤 공에서
계속 양수이고, 그 공만 적분하면 엄밀히 양수가 나와 가정에 모순이다. 음수인
경우도 같은 논증으로 배제된다.

따라서 피적분 함수는 어디서나 0 이다 — 연속이라는 단서 아래에서. 그 단서가
바로 연속체 가정의 재등장이며, 충격파를 비롯한 불연속에서는 무너진다.
그곳에서는 적분 형태가 살아남고 편미분 방정식이 살아남지 못한다.

## 1. 질량 보존

물질 영역의 질량은 변하지 않는다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \rho \, \mathrm{d}v = 0
{{< /katex >}}

{{< katex >}}\phi = \rho{{< /katex >}} 로 수송 정리를 적용하면

{{< katex display=true >}}
\int_{\Omega_t} \big(\dot{\rho} + \rho \, \nabla \cdot \mathbf{v}\big) \, \mathrm{d}v = 0
{{< /katex >}}

이고 국소화하면

{{< katex display=true >}}
\boxed{\;\dot{\rho} + \rho \, \nabla \cdot \mathbf{v} = 0\;}
{{< /katex >}}

**연속 방정식**(continuity equation)이다. 물질 미분을 펼치면 동등한 공간
형태 {{< katex >}}\partial \rho / \partial t + \nabla \cdot (\rho \mathbf{v}) = 0{{< /katex >}}
을 얻는다.

### {{< katex >}}\rho_0 = \rho J{{< /katex >}} 와의 일치

[운동학]({{< ref "kinematics.md" >}}) 은 질량 보존을 미분이 없는 대수적 명제
{{< katex >}}\rho_0 = \rho J{{< /katex >}} 로 얻었다. 둘은 일치해야 한다.
{{< katex >}}\rho_0{{< /katex >}} 는 입자에 붙어 있어 시간에 따라 변할 수
없으므로

{{< katex display=true >}}
0 = \frac{\mathrm{d}}{\mathrm{d}t}(\rho J) = \dot{\rho}J + \rho\dot{J}
= \dot{\rho}J + \rho J \nabla \cdot \mathbf{v}
= J\big(\dot{\rho} + \rho \nabla \cdot \mathbf{v}\big)
{{< /katex >}}

이고 {{< katex >}}J > 0{{< /katex >}} 이므로 괄호가 0 이다. 반대 방향에서
도달한 같은 방정식이다.

### 숫자 하나

밀도 {{< katex >}}1000 \ \mathrm{kg/m^3}{{< /katex >}} 인 젤리 덩어리를 눌러
부피를 절반으로 만든다. {{< katex >}}J = 0.5{{< /katex >}} 이므로

{{< katex display=true >}}
\rho = \frac{\rho_0}{J} = \frac{1000}{0.5} = 2000 \ \mathrm{kg/m^3}
{{< /katex >}}

부피는 절반, 밀도는 두 배, 질량은 그대로. 연속 방정식은 이것을 변화율로
말하고 {{< katex >}}\rho_0 = \rho J{{< /katex >}} 는 곧바로 말한다.

## 2. 코시 응력

운동량으로 가기 전에 내부 면에 걸리는 힘을 표현할 방법이 필요하다.

단위 법선 {{< katex >}}\mathbf{n}{{< /katex >}} 을 가진 면을 따라 물체를
자른다. 한쪽 물질이 다른 쪽을 단위 면적당 힘으로 당기고, 이를
**트랙션**(traction) {{< katex >}}\mathbf{t}{{< /katex >}} 라 한다. 이는
방향에 의존한다. 같은 점이라도 수평으로 자른 면의 트랙션과 수직으로 자른 면의
트랙션은 다르다.

코시의 결과는 그 의존성이 *선형*이라는 것이다. 세 면이 좌표평면 위에 있고
넷째 면의 법선이 {{< katex >}}\mathbf{n}{{< /katex >}} 인 작은 사면체를 생각한다.
힘의 평형을 쓰면 표면항은 {{< katex >}}L^2{{< /katex >}} 로, 체적력과 관성항은
{{< katex >}}L^3{{< /katex >}} 로 스케일한다.
{{< katex >}}L \to 0{{< /katex >}} 으로 줄이면 체적항이 더 빨리 사라지고
표면항끼리 평형을 이뤄야 한다. 남는 것은

{{< katex display=true >}}
t_i = \sigma_{ji} n_j
{{< /katex >}}

여기서 {{< katex >}}\sigma_{ji}{{< /katex >}} 는 법선이
{{< katex >}}\mathbf{e}_j{{< /katex >}} 인 면에 걸리는 트랙션의
{{< katex >}}i{{< /katex >}} 성분이다. 이것이 **코시 응력
텐서**(Cauchy stress tensor)이고, 단위 *현재* 면적당 힘 — 실험이 재는 그
응력이다.

첨자 순서는 의도적이고 잠정적이다.
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} 이라 쓰는
것이 표준이지만 그 형태는 대칭성을 전제하고, 대칭성은 아직 확립되지 않았다 —
바로 각운동량에서 유도될 참이다. 여기서 가정해 버리면 그 유도가 순환이 된다.
그래서 4절까지는 첨자를 드러낸다.

## 3. 선운동량

물질 영역에 대한 뉴턴 제2법칙이다. 운동량의 변화율은 가해진 힘과 같고, 힘은
경계의 트랙션과 중력 같은 단위 질량당 체적력
{{< katex >}}\mathbf{b}{{< /katex >}} 에서 온다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \rho \mathbf{v} \, \mathrm{d}v
= \int_{\partial\Omega_t} \mathbf{t} \, \mathrm{d}a + \int_{\Omega_t} \rho \mathbf{b} \, \mathrm{d}v
{{< /katex >}}

**좌변.** {{< katex >}}\phi = \rho v_i{{< /katex >}} 로 수송 정리를 쓴다.

{{< katex display=true >}}
\int_{\Omega_t} \Big(\dot{\rho}v_i + \rho\dot{v}_i + \rho v_i \nabla\cdot\mathbf{v}\Big) \mathrm{d}v
= \int_{\Omega_t} \Big(\rho \dot{v}_i + v_i\underbrace{\big(\dot{\rho} + \rho\nabla\cdot\mathbf{v}\big)}_{= \, 0}\Big) \mathrm{d}v
= \int_{\Omega_t} \rho \dot{v}_i \, \mathrm{d}v
{{< /katex >}}

괄호가 연속 방정식이라 사라진다. 밀도가 변할 수 있는데도 운동량 평형이
{{< katex >}}m\mathbf{a}{{< /katex >}} 처럼 생기는 이유가 이 상쇄다.

**우변.** {{< katex >}}t_i = \sigma_{ji}n_j{{< /katex >}} 를 넣고 발산 정리를
적용한다.

{{< katex display=true >}}
\int_{\partial\Omega_t} \sigma_{ji} n_j \, \mathrm{d}a = \int_{\Omega_t} \frac{\partial \sigma_{ji}}{\partial x_j} \, \mathrm{d}v
{{< /katex >}}

모아서 국소화하면

{{< katex display=true >}}
\boxed{\;\frac{\partial \sigma_{ji}}{\partial x_j} + \rho b_i = \rho \dot{v}_i\;}
\qquad\text{또는}\qquad
\nabla \cdot \boldsymbol{\sigma} + \rho \mathbf{b} = \rho \dot{\mathbf{v}}
{{< /katex >}}

**이 식이 이 분야의 중심이다.**
{{< katex >}}\dot{\mathbf{v}} = \mathbf{0}{{< /katex >}} 으로 두면 정적 평형이
되고, 모든 응력 해석이 푸는 것이 이 식이다. 또한 유한요소법이 시험 함수와
곱해 부분적분하는 잔차이고, 물리 기반 신경망이 벌하는 잔차다.

### 같은 법칙, 기준 상태에서

방금 유도한 식에는 실용적인 문제가 있다.
{{< katex >}}\Omega_t{{< /katex >}}, 즉 변형된 물체 위에서 세워졌는데 그
영역은 문제를 풀기 전에는 모른다. 대변형에서 이 순환은 치명적이다. 해법은
법칙을 아는 영역인 {{< katex >}}\Omega_0{{< /katex >}} 위에서 다시 쓰는 것이다.

면적분을 옮기려면 현재와 기준의 면적 요소를 이어야 한다. **난슨
공식**(Nanson's formula)이 그 일을 한다.

{{< katex display=true >}}
\mathbf{n} \, \mathrm{d}a = J \mathbf{F}^{-T} \mathbf{N} \, \mathrm{d}A
{{< /katex >}}

{{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}} 에서 나온다. 기준
상태 면적 요소 {{< katex >}}\mathbf{N} \, \mathrm{d}A{{< /katex >}} 와 임의의
기준 상태 벡터 {{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}} 를 잡으면 둘이
부피 {{< katex >}}\mathrm{d}V = \mathbf{N} \cdot \mathrm{d}\mathbf{X} \, \mathrm{d}A{{< /katex >}}
인 기둥을 만든다. 변형 후 같은 물질은
{{< katex >}}\mathrm{d}v = \mathbf{n} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X} \, \mathrm{d}a{{< /katex >}}
를 차지한다. {{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}} 이므로

{{< katex display=true >}}
\mathbf{n} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X} \, \mathrm{d}a = J \, \mathbf{N} \cdot \mathrm{d}\mathbf{X} \, \mathrm{d}A
\quad \Longrightarrow \quad
\mathbf{F}^T \mathbf{n} \, \mathrm{d}a = J \mathbf{N} \, \mathrm{d}A
{{< /katex >}}

가 임의의 {{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}} 에 대해 성립하고,
정리하면 난슨 공식이다.

이제 *같은 물리적 힘*을 기준 상태 면적 위에서 표현하도록 요구한다.
**제1 피올라-키르히호프 응력**(first Piola–Kirchhoff stress)
{{< katex >}}\mathbf{P}{{< /katex >}} 를 다음으로 정의한다.

{{< katex display=true >}}
\mathbf{P}\mathbf{N} \, \mathrm{d}A = \boldsymbol{\sigma}\mathbf{n} \, \mathrm{d}a
= J\boldsymbol{\sigma}\mathbf{F}^{-T}\mathbf{N} \, \mathrm{d}A
\quad \Longrightarrow \quad
\boxed{\;\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T}\;}
{{< /katex >}}

이 정의로 운동량 평형은 구조를 바꾸지 않고 기준 상태로 옮겨간다.

{{< katex display=true >}}
\nabla_0 \cdot \mathbf{P} + \rho_0 \mathbf{b} = \rho_0 \ddot{\mathbf{u}},
\qquad \frac{\partial P_{iJ}}{\partial X_J} + \rho_0 b_i = \rho_0 \ddot{u}_i
{{< /katex >}}

질량항에는
{{< katex >}}\rho \, \mathrm{d}v = \rho_0 \, \mathrm{d}V{{< /katex >}} 를 썼다.

{{< katex >}}\mathbf{P}{{< /katex >}} 는
{{< katex >}}\mathbf{F}{{< /katex >}} 의 두 점 성격을 물려받아 한 다리씩 두
상태에 걸치고, 그 결과 **대칭이 아니다**. 이는 실제로 불편한 일이며,
[응력]({{< ref "stress.md" >}}) 이 세 번째 응력 텐서로 해결한다.

### 숫자 하나

{{< katex >}}\rho_0 = 7800 \ \mathrm{kg/m^3}{{< /katex >}} 인 강판이 중력
{{< katex >}}g = 9.81 \ \mathrm{m/s^2}{{< /katex >}} 아래
{{< katex >}}-x_2{{< /katex >}} 방향으로 정지해 있다.
{{< katex >}}\dot{\mathbf{v}} = \mathbf{0}{{< /katex >}} 이므로
{{< katex >}}i = 2{{< /katex >}} 성분은

{{< katex display=true >}}
\frac{\partial \sigma_{12}}{\partial x_1} + \frac{\partial \sigma_{22}}{\partial x_2}
= \rho g = 7800 \times 9.81 = 76518 \ \mathrm{Pa/m}
{{< /katex >}}

판이 순수한 수직 응력 상태라
{{< katex >}}\sigma_{12}{{< /katex >}} 가 균일하다면
{{< katex >}}\partial\sigma_{22}/\partial x_2 = 76518 \ \mathrm{Pa/m}{{< /katex >}},
즉 깊이 1미터마다
{{< katex >}}0.077 \ \mathrm{MPa}{{< /katex >}} 가량의 압축이 더해진다. 평형은
추상이 아니다 — 높은 기둥의 아래쪽이 위쪽보다 큰 응력을 받는 이유이고, 그
기울기를 정확히 정한다.

## 4. 각운동량, 그리고 응력의 대칭성

모멘트도 평형을 이룬다.

{{< katex display=true >}}
\int_{\partial\Omega_t} (\mathbf{x} \times \mathbf{t}) \, \mathrm{d}a
+ \int_{\Omega_t} (\mathbf{x} \times \rho\mathbf{b}) \, \mathrm{d}v
= \frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} (\mathbf{x} \times \rho\mathbf{v}) \, \mathrm{d}v
{{< /katex >}}

결과는 또 하나의 미분 방정식이 아니라 대수적 제약이고, 인덱스 표기를 쓸 값이
있다 — 여기서는 외적 때문에 직접 표기가 다루기 어렵다.

레비-치비타 기호(Levi-Civita symbol)
{{< katex >}}\epsilon_{ijk}{{< /katex >}} 로
{{< katex >}}(\mathbf{a} \times \mathbf{b})_i = \epsilon_{ijk}a_j b_k{{< /katex >}}
라 쓴다. {{< katex >}}\epsilon_{ijk}{{< /katex >}} 는
{{< katex >}}(1,2,3){{< /katex >}} 의 짝치환이면
{{< katex >}}+1{{< /katex >}}, 홀치환이면
{{< katex >}}-1{{< /katex >}}, 첨자가 겹치면
{{< katex >}}0{{< /katex >}} 이다.

면적분에 {{< katex >}}t_k = \sigma_{pk}n_p{{< /katex >}} 를 넣고 발산 정리를
적용한다.

{{< katex display=true >}}
\int_{\partial\Omega_t} \epsilon_{ijk}x_j \sigma_{pk} n_p \, \mathrm{d}a
= \int_{\Omega_t} \big(\epsilon_{ijk}x_j\sigma_{pk}\big)_{,p} \, \mathrm{d}v
{{< /katex >}}

곱의 미분법으로 전개한다. 핵심 단순화는
{{< katex >}}x_{j,p} = \partial x_j/\partial x_p = \delta_{jp}{{< /katex >}} —
위치를 위치로 미분한 것 — 이다.

{{< katex display=true >}}
\epsilon_{ijk}\big(x_j\sigma_{pk}\big)_{,p}
= \epsilon_{ijk}\big(\delta_{jp}\sigma_{pk} + x_j\sigma_{pk,p}\big)
= \epsilon_{ijk}\sigma_{jk} + \epsilon_{ijk}x_j\sigma_{pk,p}
{{< /katex >}}

좌변은 앞과 똑같이 수송 정리로 다루면
{{< katex >}}\int \epsilon_{ijk}x_j\rho\dot{v}_k \, \mathrm{d}v{{< /katex >}} 가
된다. {{< katex >}}\mathbf{x}{{< /katex >}} 를 미분해서 나오는 여분의 항은
{{< katex >}}\epsilon_{ijk}v_j\rho v_k{{< /katex >}} 인데,
{{< katex >}}\epsilon_{ijk}{{< /katex >}} 가
{{< katex >}}j,k{{< /katex >}} 에 대해 반대칭이고
{{< katex >}}v_jv_k{{< /katex >}} 가 대칭이라 사라진다.

전부 하나의 체적 적분으로 모으면

{{< katex display=true >}}
\int_{\Omega_t} \Big(\epsilon_{ijk}\sigma_{jk}
+ \epsilon_{ijk}x_j\underbrace{\big(\sigma_{pk,p} + \rho b_k - \rho\dot{v}_k\big)}_{=\,0}\Big) \mathrm{d}v = 0
{{< /katex >}}

밑줄 친 괄호는 3절의 선운동량 평형이라 항등적으로 0 이다 — 각운동량은 응력의
*구배*에 대해 새로운 것을 주지 않는다. 국소화 후 남는 것은

{{< katex display=true >}}
\epsilon_{ijk}\sigma_{jk} = 0
{{< /katex >}}

{{< katex >}}i = 1{{< /katex >}} 로 두면 살아남는 항은
{{< katex >}}\epsilon_{123}\sigma_{23} + \epsilon_{132}\sigma_{32} = \sigma_{23} - \sigma_{32} = 0{{< /katex >}}
이다. 나머지 두 성분이 남은 쌍을 주므로

{{< katex display=true >}}
\boxed{\;\sigma_{jk} = \sigma_{kj}, \qquad \boldsymbol{\sigma} = \boldsymbol{\sigma}^T\;}
{{< /katex >}}

**코시 응력은 대칭이다.** 아홉 개의 성분이 여섯 개로 줄고, 이제부터
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} 을 모호함
없이 쓸 수 있다. 이 대칭성은 끊임없이 쓰인다. 주응력을 실수로 만들고,
[응력]({{< ref "stress.md" >}}) 에서 {{< katex >}}\mathbf{S}{{< /katex >}} 를 대칭으로 만들고,
아래 에너지 평형에서 스핀항을 죽인다.

### 비대칭 응력이 불가능한 이유

형식적 유도가 단순한 역학적 사실을 가릴 수 있다. 한 변이
{{< katex >}}L{{< /katex >}} 인 정육면체에서
{{< katex >}}\sigma_{12} \neq \sigma_{21}{{< /katex >}} 이라 하자. 마주 보는
면의 전단 트랙션이 상쇄되지 않는 짝힘을 이루어 알짜 토크가 남는다.

{{< katex display=true >}}
T \sim (\sigma_{12} - \sigma_{21}) L^2 \cdot L = O(L^3)
{{< /katex >}}

트랙션 곱하기 면적 {{< katex >}}L^2{{< /katex >}} 곱하기 모멘트 팔
{{< katex >}}L{{< /katex >}} 이다. 한편 정육면체의 관성 모멘트는

{{< katex display=true >}}
I \sim \rho L^3 \cdot L^2 = O(L^5)
{{< /katex >}}

질량 {{< katex >}}\rho L^3{{< /katex >}} 곱하기 길이 제곱이다. 따라서 각가속도는

{{< katex display=true >}}
\alpha = \frac{T}{I} = O(L^{-2}) \xrightarrow{\;L \to 0\;} \infty
{{< /katex >}}

아무리 작은 불균형이라도 미소 요소를 무한대의 각가속도로 돌린다. 물질은 그런
짓을 하지 않으므로 불균형은 존재할 수 없다. 지수의 차이 — 3 대 5 — 가 논증의
전부이고, 제약이 근사가 아니라 정확한 이유가 그것이다.

## 5. 열역학 제1법칙

영역에 공급된 에너지는 영역이 가진 에너지의 변화와 같다. 기계적 일률은
트랙션과 체적력으로 들어오고, 열은 경계를 가로지르는 플럭스
{{< katex >}}\mathbf{q}{{< /katex >}} 와 단위 질량당 공급
{{< katex >}}r{{< /katex >}} 로 들어온다. 저장된 에너지는 운동 에너지와 내부
에너지의 합이며, 내부 에너지 밀도는 단위 질량당
{{< katex >}}e{{< /katex >}} 다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t}\Big(\tfrac{1}{2}\rho\,\mathbf{v}\cdot\mathbf{v} + \rho e\Big)\mathrm{d}v
= \int_{\partial\Omega_t}\mathbf{t}\cdot\mathbf{v}\,\mathrm{d}a
+ \int_{\Omega_t}\rho\,\mathbf{b}\cdot\mathbf{v}\,\mathrm{d}v
- \int_{\partial\Omega_t}\mathbf{q}\cdot\mathbf{n}\,\mathrm{d}a
+ \int_{\Omega_t}\rho r\,\mathrm{d}v
{{< /katex >}}

플럭스의 음부호는 약속이다.
{{< katex >}}\mathbf{q}{{< /katex >}} 는 *나가는* 열의 방향을 향한다.

트랙션 일률을 다룬다. 이제 정당해진
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} 과 발산
정리를 쓰면

{{< katex display=true >}}
\int_{\partial\Omega_t} \mathbf{v}\cdot\boldsymbol{\sigma}\mathbf{n} \, \mathrm{d}a
= \int_{\Omega_t} \nabla\cdot\big(\boldsymbol{\sigma}\mathbf{v}\big) \, \mathrm{d}v
= \int_{\Omega_t} \Big(\big(\nabla\cdot\boldsymbol{\sigma}\big)\cdot\mathbf{v} + \boldsymbol{\sigma}:\nabla\mathbf{v}\Big) \mathrm{d}v
{{< /katex >}}

여기서 {{< katex >}}\mathbf{A}:\mathbf{B} = A_{ij}B_{ij}{{< /katex >}} 는 이중
축약이다.

이제 [운동학]({{< ref "kinematics.md" >}}) 의 분해
{{< katex >}}\nabla\mathbf{v} = \mathbf{L} = \mathbf{D} + \mathbf{W}{{< /katex >}}
가 값을 한다. {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 는 대칭이고
{{< katex >}}\mathbf{W}{{< /katex >}} 는 반대칭이므로 둘의 축약은 사라진다.

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{W} = \sigma_{ij}W_{ij} = \sigma_{ji}(-W_{ji}) = -\boldsymbol{\sigma}:\mathbf{W} = 0
{{< /katex >}}

가운데 단계에서 더미 첨자를 바꿔 붙였다. 따라서

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{L} = \boldsymbol{\sigma}:\mathbf{D}
{{< /katex >}}

**강체 회전에는 에너지가 들지 않는다.** 그것이 물리적 내용이고, 방금 각운동량에서
유도한 대칭성의 직접적인 결과다.

마지막으로 기계적 에너지 항등식 — 선운동량 평형에
{{< katex >}}\mathbf{v}{{< /katex >}} 를 내적해 적분한 것, 즉
{{< katex >}}\int (\nabla\cdot\boldsymbol{\sigma} + \rho\mathbf{b})\cdot\mathbf{v} = \int \rho\dot{\mathbf{v}}\cdot\mathbf{v}{{< /katex >}}
— 를 빼면 양변에서 운동 에너지 항과 응력 발산 항이 상쇄되고, 국소화 후

{{< katex display=true >}}
\boxed{\;\rho\dot{e} = \boldsymbol{\sigma}:\mathbf{D} - \nabla\cdot\mathbf{q} + \rho r\;}
{{< /katex >}}

{{< katex >}}\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}} 항이 **응력
일률**(stress power)이다. 단위 현재 부피당, 변형이 재료에 에너지를 넣는
비율이다. 뒤따르는 모든 것으로 가는 다리이며, [응력]({{< ref "stress.md" >}}) 은 이것이 세 개의
동등한 형태를 갖는다는 것을, [구성 방정식]({{< ref "constitutive.md" >}}) 은 에너지 함수를
미분해 응력을 얻는 근거가 바로 이 항이라는 것을 보인다.

## 셈이 남긴 것

이제 네 법칙이 있다. 질량에서 스칼라 방정식 하나, 선운동량에서 셋,
각운동량에서 대칭 제약, 에너지에서 스칼라 하나.

열적 효과를 빼고 미지수와 방정식을 센다. 미지수는
{{< katex >}}\rho{{< /katex >}}(1),
{{< katex >}}\mathbf{v}{{< /katex >}}(3),
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}}(대칭성 이후 6) — 열 개. 방정식은
질량(1)과 운동량(3) — 네 개.

**여섯 개가 모자란다.** 보존 법칙을 아무리 더 다뤄도 그 틈은 메워지지 않는다.
그 틈이 바로 재료가 아직 지정되지 않은 자리이기 때문이다. 메우는 일은
[구성 방정식]({{< ref "constitutive.md" >}}) 의 몫이다.

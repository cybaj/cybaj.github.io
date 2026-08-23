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

명제는 네 개입니다. 질량은 보존되고, 선운동량은 평형을 이루며, 각운동량도
평형을 이루고, 에너지는 보존됩니다. 어느 것도 특정한 재료에 관한 이야기가 아니어서
강철이든 고무든 물이든 똑같이 따릅니다. 이들을 갈라놓는 요소는
[구성 방정식]({{< ref "constitutive.md" >}})까지 등장하지 않습니다.
(개인 노트: preparation 1 : 기본 보존 법칙)

각 법칙은 유한한 크기의 물질 덩어리에 대한 진술로 시작해서 모든 점에서
성립하는 편미분 방정식으로 끝납니다. 그 변환에 쓰이는 도구가 매번 같으므로
그것부터 준비하겠습니다.

## 준비물 두 가지

### 레이놀즈 수송 정리

보존 법칙이 말하는 것은 *물질* 영역이 담고 있는 양의 변화율입니다. 물질
영역은 언제나 같은 입자들로 이루어져 있으므로 그 경계가 함께 움직입니다.
움직이는 영역 위의 적분을 미분하는 일은 만만치 않습니다. 피적분 함수도 적분
영역도 시간에 따라 변하기 때문입니다.

요령은 영역을 고정시키는 것입니다. 임의의 공간 장
{{< katex >}}\phi(\mathbf{x}, t){{< /katex >}} 에 대해
{{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}} 를 이용해 적분을
움직이지 않는 기준 상태로 옮깁니다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \phi \, \mathrm{d}v
= \frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_0} \phi J \, \mathrm{d}V
= \int_{\Omega_0} \frac{\mathrm{d}}{\mathrm{d}t}(\phi J) \, \mathrm{d}V
{{< /katex >}}

미분과 적분의 순서를 바꿀 수 있는 것은
{{< katex >}}\Omega_0{{< /katex >}} 가 시간에 대해 고정되어 있기 때문입니다.
곱의 미분법으로 전개하고 [운동학]({{< ref "kinematics.md" >}})에서 얻은
{{< katex >}}\dot{J} = J \nabla \cdot \mathbf{v}{{< /katex >}} 를 넣습니다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}(\phi J) = \dot{\phi} J + \phi \dot{J}
= J\big(\dot{\phi} + \phi \, \nabla \cdot \mathbf{v}\big)
{{< /katex >}}

{{< katex >}}J \, \mathrm{d}V = \mathrm{d}v{{< /katex >}} 로 다시 되돌리면

{{< katex display=true >}}
\boxed{\;\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \phi \, \mathrm{d}v
= \int_{\Omega_t} \big(\dot{\phi} + \phi \, \nabla \cdot \mathbf{v}\big) \, \mathrm{d}v\;}
{{< /katex >}}

이것이 **레이놀즈 수송 정리**(Reynolds transport theorem)입니다. 첫째 항은
양 자체가 변해서 생기는 몫이고, 둘째 항은 영역이 커지거나 작아져서 생기는
몫입니다.

### 국소화

아래의 유도는 모두
{{< katex >}}\int_{\Omega_t} (\cdots) \, \mathrm{d}v = 0{{< /katex >}} 형태에
도달한 다음, 피적분 함수가 점마다 0 이라고 결론짓습니다. 이 단계의 근거는 한
번은 짚고 넘어가야 합니다.

적분이 0 인 것은 어느 한 영역에 대해서가 아니라 *모든* 물질 영역에
대해서입니다. 보존 법칙이 애초에 특정 덩어리를 두고 한 말이 아니기
때문입니다. 어떤 점 {{< katex >}}\mathbf{x}_0{{< /katex >}} 에서 피적분 함수가
양수라고 해 보겠습니다. 연속이므로 그 점 주위의 작은 공 안에서도 계속 양수일
것이고, 그 공만 적분하면 0 보다 큰 값이 나와 가정과 어긋납니다. 음수인 경우도
같은 방식으로 배제됩니다.

따라서 피적분 함수는 어디서나 0 입니다. 단, 연속이라는 조건이 붙습니다. 이
조건은 결국 연속체 가정이 다시 등장한 것이며, 충격파처럼 불연속이 있는
곳에서는 성립하지 않습니다. 그런 곳에서는 적분 형태만 살아남고 편미분 방정식은
살아남지 못합니다.

## 1. 질량 보존

물질 영역의 질량은 변하지 않습니다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \rho \, \mathrm{d}v = 0
{{< /katex >}}

{{< katex >}}\phi = \rho{{< /katex >}} 로 두고 수송 정리를 쓰면

{{< katex display=true >}}
\int_{\Omega_t} \big(\dot{\rho} + \rho \, \nabla \cdot \mathbf{v}\big) \, \mathrm{d}v = 0
{{< /katex >}}

이고, 국소화하면

{{< katex display=true >}}
\boxed{\;\dot{\rho} + \rho \, \nabla \cdot \mathbf{v} = 0\;}
{{< /katex >}}

**연속 방정식**(continuity equation)입니다. 물질 미분을 풀어 쓰면 공간 형태
{{< katex >}}\partial \rho / \partial t + \nabla \cdot (\rho \mathbf{v}) = 0{{< /katex >}}
과 같습니다.

### 대수적 형태와 어긋나지 않는가

[운동학]({{< ref "kinematics.md" >}})에서는 질량 보존을 미분이 없는 관계식
{{< katex >}}\rho_0 = \rho J{{< /katex >}} 로 얻었습니다. 두 결과는 같아야
합니다. {{< katex >}}\rho_0{{< /katex >}} 는 입자에 붙어 있는 값이라 시간에
따라 변할 수 없으므로

{{< katex display=true >}}
0 = \frac{\mathrm{d}}{\mathrm{d}t}(\rho J) = \dot{\rho}J + \rho\dot{J}
= \dot{\rho}J + \rho J \nabla \cdot \mathbf{v}
= J\big(\dot{\rho} + \rho \nabla \cdot \mathbf{v}\big)
{{< /katex >}}

이고 {{< katex >}}J > 0{{< /katex >}} 이므로 괄호 안이 0 입니다. 반대편에서
출발했지만 같은 식에 도착한 것입니다.

### 숫자로 확인하기

밀도가 {{< katex >}}1000 \ \mathrm{kg/m^3}{{< /katex >}} 인 젤리 덩어리를
눌러 부피를 절반으로 만들어 보겠습니다.
{{< katex >}}J = 0.5{{< /katex >}} 이므로

{{< katex display=true >}}
\rho = \frac{\rho_0}{J} = \frac{1000}{0.5} = 2000 \ \mathrm{kg/m^3}
{{< /katex >}}

부피는 절반이 되고 밀도는 두 배가 되며 질량은 그대로입니다.
(개인 노트: preparation 1 : 기본 보존 법칙) 연속 방정식은 이 사실을 변화율의
언어로 말하고, {{< katex >}}\rho_0 = \rho J{{< /katex >}} 는 한 줄로
말합니다.

## 2. 코시 응력

운동량으로 넘어가기 전에, 물체 내부의 면에 걸리는 힘을 표현할 방법이
필요합니다.

단위 법선이 {{< katex >}}\mathbf{n}{{< /katex >}} 인 면을 따라 물체를
자릅니다. 한쪽 물질이 다른 쪽을 단위 면적당 얼마의 힘으로 당기는지를
**트랙션**(traction) {{< katex >}}\mathbf{t}{{< /katex >}} 라 합니다. 이 값은
자른 방향에 따라 달라져서, 같은 점이라도 가로로 자른 면과 세로로 자른 면의
트랙션이 다릅니다.

코시가 밝힌 것은 그 의존성이 *선형*이라는 사실입니다. 세 면은 좌표평면 위에
놓이고 나머지 한 면의 법선이 {{< katex >}}\mathbf{n}{{< /katex >}} 인 작은
사면체를 생각해 보겠습니다. 힘의 평형을 쓰면 표면에 관한 항은
{{< katex >}}L^2{{< /katex >}} 에, 체적력과 관성에 관한 항은
{{< katex >}}L^3{{< /katex >}} 에 비례합니다.
{{< katex >}}L \to 0{{< /katex >}} 으로 줄이면 체적 쪽이 훨씬 빨리 작아지므로
표면 쪽 항들끼리 평형을 이뤄야 하고, 그 결과

{{< katex display=true >}}
t_i = \sigma_{ji} n_j
{{< /katex >}}

가 남습니다. {{< katex >}}\sigma_{ji}{{< /katex >}} 는 법선이
{{< katex >}}\mathbf{e}_j{{< /katex >}} 인 면에 걸리는 트랙션의
{{< katex >}}i{{< /katex >}} 성분입니다. 이것을 **코시 응력 텐서**(Cauchy
stress tensor)라 하며, 단위 *현재* 면적당 힘, 즉 실험에서 실제로 재는
응력입니다.

첨자 순서를 이렇게 적은 데는 이유가 있고, 잠시뿐입니다. 보통은
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} 이라
쓰지만 그 표기는 대칭성을 전제합니다. 그런데 대칭성은 아직 증명되지 않았고,
바로 다음의 각운동량에서 유도할 참입니다. 여기서 미리 가정해 버리면 그 유도가
순환 논증이 되므로, 4절까지는 첨자를 그대로 드러냅니다.

## 3. 선운동량

물질 영역에 뉴턴 제2법칙을 적용한 것입니다. 운동량의 변화율은 가해진 힘과
같고, 힘은 경계에 걸리는 트랙션과 중력 같은 단위 질량당 체적력
{{< katex >}}\mathbf{b}{{< /katex >}} 에서 옵니다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \rho \mathbf{v} \, \mathrm{d}v
= \int_{\partial\Omega_t} \mathbf{t} \, \mathrm{d}a + \int_{\Omega_t} \rho \mathbf{b} \, \mathrm{d}v
{{< /katex >}}

**좌변부터.** {{< katex >}}\phi = \rho v_i{{< /katex >}} 로 두고 수송 정리를
씁니다.

{{< katex display=true >}}
\int_{\Omega_t} \Big(\dot{\rho}v_i + \rho\dot{v}_i + \rho v_i \nabla\cdot\mathbf{v}\Big) \mathrm{d}v
= \int_{\Omega_t} \Big(\rho \dot{v}_i + v_i\underbrace{\big(\dot{\rho} + \rho\nabla\cdot\mathbf{v}\big)}_{= \, 0}\Big) \mathrm{d}v
= \int_{\Omega_t} \rho \dot{v}_i \, \mathrm{d}v
{{< /katex >}}

묶인 괄호가 연속 방정식이라 통째로 사라집니다. 밀도가 얼마든지 변할 수
있는데도 운동량 평형이 결국 {{< katex >}}m\mathbf{a}{{< /katex >}} 꼴로
정리되는 것은 이 상쇄 덕분입니다.

**우변.** {{< katex >}}t_i = \sigma_{ji}n_j{{< /katex >}} 를 넣고 발산 정리를
씁니다.

{{< katex display=true >}}
\int_{\partial\Omega_t} \sigma_{ji} n_j \, \mathrm{d}a = \int_{\Omega_t} \frac{\partial \sigma_{ji}}{\partial x_j} \, \mathrm{d}v
{{< /katex >}}

둘을 합치고 국소화하면

{{< katex display=true >}}
\boxed{\;\frac{\partial \sigma_{ji}}{\partial x_j} + \rho b_i = \rho \dot{v}_i\;}
\qquad\text{또는}\qquad
\nabla \cdot \boldsymbol{\sigma} + \rho \mathbf{b} = \rho \dot{\mathbf{v}}
{{< /katex >}}

이 식이 연속체 역학의 중심에 있습니다.
{{< katex >}}\dot{\mathbf{v}} = \mathbf{0}{{< /katex >}} 으로 두면 정적 평형이
되고, 모든 응력 해석이 결국 푸는 것이 이 식입니다. 유한요소법이 시험 함수와
곱해 부분적분하는 대상도, 물리 기반 신경망이 손실 함수에서 벌점을 매기는
대상도 같은 식입니다.

### 기준 상태에서 다시 쓰기

방금 얻은 식에는 현실적인 문제가 있습니다. 변형된 물체
{{< katex >}}\Omega_t{{< /katex >}} 위에서 세워졌는데, 그 영역은 문제를 풀기
전에는 알 수 없습니다. 대변형에서는 이 순환이 치명적입니다. 해결책은 이미 알고
있는 영역인 {{< katex >}}\Omega_0{{< /katex >}} 위에서 법칙을 다시 쓰는
것입니다.

면적분을 옮기려면 현재 면적 요소와 기준 면적 요소를 이어 주는 관계가
필요합니다. **난슨 공식**(Nanson's formula)이 그 역할을 합니다.

{{< katex display=true >}}
\mathbf{n} \, \mathrm{d}a = J \mathbf{F}^{-T} \mathbf{N} \, \mathrm{d}A
{{< /katex >}}

유도는 {{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}} 에서
출발합니다. 기준 상태의 면적 요소
{{< katex >}}\mathbf{N} \, \mathrm{d}A{{< /katex >}} 와 임의의 벡터
{{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}} 를 잡으면 이 둘이 부피
{{< katex >}}\mathrm{d}V = \mathbf{N} \cdot \mathrm{d}\mathbf{X} \, \mathrm{d}A{{< /katex >}}
인 기둥을 이룹니다. 변형 후 같은 물질이 차지하는 부피는
{{< katex >}}\mathrm{d}v = \mathbf{n} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X} \, \mathrm{d}a{{< /katex >}}
이고, {{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}} 이므로

{{< katex display=true >}}
\mathbf{n} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X} \, \mathrm{d}a = J \, \mathbf{N} \cdot \mathrm{d}\mathbf{X} \, \mathrm{d}A
\quad \Longrightarrow \quad
\mathbf{F}^T \mathbf{n} \, \mathrm{d}a = J \mathbf{N} \, \mathrm{d}A
{{< /katex >}}

가 임의의 {{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}} 에 대해 성립하고,
정리하면 난슨 공식이 됩니다.

이제 *같은 힘*을 기준 상태의 면적으로 나누어 표현하겠습니다.
**제1 피올라-키르히호프 응력**(first Piola–Kirchhoff stress)
{{< katex >}}\mathbf{P}{{< /katex >}} 를 다음과 같이 정의합니다.

{{< katex display=true >}}
\mathbf{P}\mathbf{N} \, \mathrm{d}A = \boldsymbol{\sigma}\mathbf{n} \, \mathrm{d}a
= J\boldsymbol{\sigma}\mathbf{F}^{-T}\mathbf{N} \, \mathrm{d}A
\quad \Longrightarrow \quad
\boxed{\;\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T}\;}
{{< /katex >}}

이 정의 덕분에 운동량 평형은 모양을 그대로 유지한 채 기준 상태로 옮겨
갑니다.

{{< katex display=true >}}
\nabla_0 \cdot \mathbf{P} + \rho_0 \mathbf{b} = \rho_0 \ddot{\mathbf{u}},
\qquad \frac{\partial P_{iJ}}{\partial X_J} + \rho_0 b_i = \rho_0 \ddot{u}_i
{{< /katex >}}

질량에 관한 항에는
{{< katex >}}\rho \, \mathrm{d}v = \rho_0 \, \mathrm{d}V{{< /katex >}} 를
썼습니다.

{{< katex >}}\mathbf{P}{{< /katex >}} 는
{{< katex >}}\mathbf{F}{{< /katex >}} 의 두 점 성격을 그대로 물려받아 한 발은
기준 상태에, 한 발은 현재 상태에 걸치고 있습니다. 그래서 대칭이 아닌데,
실제로 불편한 성질이라 [응력]({{< ref "stress.md" >}})에서 세 번째 응력
텐서를 도입해 해결합니다.

### 숫자로 확인하기

{{< katex >}}\rho_0 = 7800 \ \mathrm{kg/m^3}{{< /katex >}} 인 강판이 중력
{{< katex >}}g = 9.81 \ \mathrm{m/s^2}{{< /katex >}} 아래
{{< katex >}}-x_2{{< /katex >}} 방향으로 정지해 있다고 하겠습니다.
{{< katex >}}\dot{\mathbf{v}} = \mathbf{0}{{< /katex >}} 이므로
{{< katex >}}i = 2{{< /katex >}} 성분은 다음과 같습니다.
(개인 노트: preparation 1 : 기본 보존 법칙)

{{< katex display=true >}}
\frac{\partial \sigma_{12}}{\partial x_1} + \frac{\partial \sigma_{22}}{\partial x_2}
= \rho g = 7800 \times 9.81 = 76518 \ \mathrm{Pa/m}
{{< /katex >}}

판이 수직 응력만 받는 상태여서
{{< katex >}}\sigma_{12}{{< /katex >}} 가 일정하다면
{{< katex >}}\partial\sigma_{22}/\partial x_2 = 76518 \ \mathrm{Pa/m}{{< /katex >}},
즉 깊이 1미터마다 {{< katex >}}0.077 \ \mathrm{MPa}{{< /katex >}} 정도씩
압축이 더해집니다. 평형 방정식은 추상적인 이야기가 아닙니다. 높은 기둥의
아래쪽이 위쪽보다 큰 응력을 받는 이유이고, 그 증가율까지 정확히 정해 줍니다.

## 4. 각운동량과 응력의 대칭성

모멘트도 평형을 이룹니다.

{{< katex display=true >}}
\int_{\partial\Omega_t} (\mathbf{x} \times \mathbf{t}) \, \mathrm{d}a
+ \int_{\Omega_t} (\mathbf{x} \times \rho\mathbf{b}) \, \mathrm{d}v
= \frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} (\mathbf{x} \times \rho\mathbf{v}) \, \mathrm{d}v
{{< /katex >}}

여기서 나오는 것은 또 하나의 미분 방정식이 아니라 대수적인 제약입니다. 외적
때문에 직접 표기로는 다루기 번거로우므로 인덱스 표기를 쓰겠습니다.

레비-치비타 기호(Levi-Civita symbol)
{{< katex >}}\epsilon_{ijk}{{< /katex >}} 를 써서
{{< katex >}}(\mathbf{a} \times \mathbf{b})_i = \epsilon_{ijk}a_j b_k{{< /katex >}}
라 씁니다. {{< katex >}}\epsilon_{ijk}{{< /katex >}} 는
{{< katex >}}(1,2,3){{< /katex >}} 의 짝치환이면
{{< katex >}}+1{{< /katex >}}, 홀치환이면
{{< katex >}}-1{{< /katex >}}, 첨자가 겹치면 0 입니다.

면적분에 {{< katex >}}t_k = \sigma_{pk}n_p{{< /katex >}} 를 넣고 발산 정리를
씁니다.

{{< katex display=true >}}
\int_{\partial\Omega_t} \epsilon_{ijk}x_j \sigma_{pk} n_p \, \mathrm{d}a
= \int_{\Omega_t} \big(\epsilon_{ijk}x_j\sigma_{pk}\big)_{,p} \, \mathrm{d}v
{{< /katex >}}

곱의 미분법으로 전개합니다. 이때 중요한 것은
{{< katex >}}x_{j,p} = \partial x_j/\partial x_p = \delta_{jp}{{< /katex >}},
즉 위치를 위치로 미분한 결과입니다.

{{< katex display=true >}}
\epsilon_{ijk}\big(x_j\sigma_{pk}\big)_{,p}
= \epsilon_{ijk}\big(\delta_{jp}\sigma_{pk} + x_j\sigma_{pk,p}\big)
= \epsilon_{ijk}\sigma_{jk} + \epsilon_{ijk}x_j\sigma_{pk,p}
{{< /katex >}}

좌변은 앞서와 똑같이 수송 정리로 처리하면
{{< katex >}}\int \epsilon_{ijk}x_j\rho\dot{v}_k \, \mathrm{d}v{{< /katex >}} 가
됩니다. {{< katex >}}\mathbf{x}{{< /katex >}} 를 미분하면서 생기는 여분의 항
{{< katex >}}\epsilon_{ijk}v_j\rho v_k{{< /katex >}} 는
{{< katex >}}\epsilon_{ijk}{{< /katex >}} 가
{{< katex >}}j, k{{< /katex >}} 에 대해 반대칭인데
{{< katex >}}v_jv_k{{< /katex >}} 는 대칭이라 저절로 사라집니다.

전부 하나의 체적 적분으로 모으면

{{< katex display=true >}}
\int_{\Omega_t} \Big(\epsilon_{ijk}\sigma_{jk}
+ \epsilon_{ijk}x_j\underbrace{\big(\sigma_{pk,p} + \rho b_k - \rho\dot{v}_k\big)}_{=\,0}\Big) \mathrm{d}v = 0
{{< /katex >}}

묶인 부분은 3절의 선운동량 평형이므로 항등적으로 0 입니다. 각운동량에서
응력의 *기울기*에 관한 새로운 정보는 나오지 않는다는 뜻입니다. 국소화하고 나면

{{< katex display=true >}}
\epsilon_{ijk}\sigma_{jk} = 0
{{< /katex >}}

만 남습니다. {{< katex >}}i = 1{{< /katex >}} 로 두면 살아남는 항이
{{< katex >}}\epsilon_{123}\sigma_{23} + \epsilon_{132}\sigma_{32} = \sigma_{23} - \sigma_{32} = 0{{< /katex >}}
이고, 나머지 두 성분이 남은 짝을 줍니다. 따라서

{{< katex display=true >}}
\boxed{\;\sigma_{jk} = \sigma_{kj}, \qquad \boldsymbol{\sigma} = \boldsymbol{\sigma}^T\;}
{{< /katex >}}

코시 응력은 대칭입니다. 성분이 아홉 개에서 여섯 개로 줄고, 이제부터는
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} 이라 써도
모호하지 않습니다. 이 대칭성은 앞으로 계속 쓰입니다. 주응력이 실수가 되는 것도,
[응력]({{< ref "stress.md" >}})에서 {{< katex >}}\mathbf{S}{{< /katex >}} 가
대칭이 되는 것도, 아래 에너지 평형에서 스핀 항이 사라지는 것도 모두 여기서
나옵니다.

### 비대칭 응력이 있을 수 없는 이유

형식적인 유도만 보면 정작 단순한 역학적 사실이 가려집니다. 한 변이
{{< katex >}}L{{< /katex >}} 인 정육면체에서
{{< katex >}}\sigma_{12} \neq \sigma_{21}{{< /katex >}} 이라고 해 보겠습니다.
마주 보는 면의 전단 트랙션이 서로 상쇄되지 않는 짝힘을 이루어 알짜 토크가
남습니다.

{{< katex display=true >}}
T \sim (\sigma_{12} - \sigma_{21}) L^2 \cdot L = O(L^3)
{{< /katex >}}

트랙션에 면적 {{< katex >}}L^2{{< /katex >}} 와 모멘트 팔
{{< katex >}}L{{< /katex >}} 을 곱한 값입니다. 한편 정육면체의 관성 모멘트는

{{< katex display=true >}}
I \sim \rho L^3 \cdot L^2 = O(L^5)
{{< /katex >}}

질량 {{< katex >}}\rho L^3{{< /katex >}} 에 길이의 제곱을 곱한 값입니다.
따라서 각가속도는

{{< katex display=true >}}
\alpha = \frac{T}{I} = O(L^{-2}) \xrightarrow{\;L \to 0\;} \infty
{{< /katex >}}

아무리 작은 불균형이라도 미소 요소를 무한대의 각가속도로 돌려 버립니다.
물질은 그렇게 행동하지 않으므로 불균형은 존재할 수 없습니다. 지수의 차이, 즉
3 과 5 의 차이가 논증의 전부이며, 이 제약이 근사가 아니라 정확한 이유도 거기에
있습니다.

## 5. 열역학 제1법칙

영역에 들어온 에너지는 그 영역이 가진 에너지의 변화와 같습니다. 기계적
일률은 트랙션과 체적력을 통해, 열은 경계를 지나는 플럭스
{{< katex >}}\mathbf{q}{{< /katex >}} 와 단위 질량당 공급량
{{< katex >}}r{{< /katex >}} 을 통해 들어옵니다. 저장된 에너지는 운동 에너지와
내부 에너지의 합이고, 내부 에너지 밀도는 단위 질량당
{{< katex >}}e{{< /katex >}} 입니다.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t}\Big(\tfrac{1}{2}\rho\,\mathbf{v}\cdot\mathbf{v} + \rho e\Big)\mathrm{d}v
= \int_{\partial\Omega_t}\mathbf{t}\cdot\mathbf{v}\,\mathrm{d}a
+ \int_{\Omega_t}\rho\,\mathbf{b}\cdot\mathbf{v}\,\mathrm{d}v
- \int_{\partial\Omega_t}\mathbf{q}\cdot\mathbf{n}\,\mathrm{d}a
+ \int_{\Omega_t}\rho r\,\mathrm{d}v
{{< /katex >}}

플럭스 앞의 음부호는 약속입니다.
{{< katex >}}\mathbf{q}{{< /katex >}} 는 열이 *빠져나가는* 방향을 향합니다.

트랙션에 의한 일률을 정리하겠습니다. 이제 정당해진
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} 과 발산
정리를 쓰면

{{< katex display=true >}}
\int_{\partial\Omega_t} \mathbf{v}\cdot\boldsymbol{\sigma}\mathbf{n} \, \mathrm{d}a
= \int_{\Omega_t} \nabla\cdot\big(\boldsymbol{\sigma}\mathbf{v}\big) \, \mathrm{d}v
= \int_{\Omega_t} \Big(\big(\nabla\cdot\boldsymbol{\sigma}\big)\cdot\mathbf{v} + \boldsymbol{\sigma}:\nabla\mathbf{v}\Big) \mathrm{d}v
{{< /katex >}}

{{< katex >}}\mathbf{A}:\mathbf{B} = A_{ij}B_{ij}{{< /katex >}} 는 이중
축약입니다.

여기서 [운동학]({{< ref "kinematics.md" >}})의 분해
{{< katex >}}\nabla\mathbf{v} = \mathbf{L} = \mathbf{D} + \mathbf{W}{{< /katex >}}
가 힘을 발휘합니다. {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 는 대칭이고
{{< katex >}}\mathbf{W}{{< /katex >}} 는 반대칭이므로 둘의 축약은 사라집니다.

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{W} = \sigma_{ij}W_{ij} = \sigma_{ji}(-W_{ji}) = -\boldsymbol{\sigma}:\mathbf{W} = 0
{{< /katex >}}

가운데 단계에서 더미 첨자를 바꿔 붙였습니다. 결국

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{L} = \boldsymbol{\sigma}:\mathbf{D}
{{< /katex >}}

회전에는 에너지가 들지 않습니다. 이것이 이 식의 물리적 내용이고, 방금
각운동량에서 얻은 대칭성이 곧바로 만들어 낸 결과입니다.

마지막으로 기계적 에너지 항등식을 뺍니다. 선운동량 평형에
{{< katex >}}\mathbf{v}{{< /katex >}} 를 내적해 적분한
{{< katex >}}\int (\nabla\cdot\boldsymbol{\sigma} + \rho\mathbf{b})\cdot\mathbf{v} = \int \rho\dot{\mathbf{v}}\cdot\mathbf{v}{{< /katex >}}
이 그것입니다. 양변에서 운동 에너지 항과 응력 발산 항이 상쇄되고,
국소화하면

{{< katex display=true >}}
\boxed{\;\rho\dot{e} = \boldsymbol{\sigma}:\mathbf{D} - \nabla\cdot\mathbf{q} + \rho r\;}
{{< /katex >}}

{{< katex >}}\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}} 를 **응력
일률**(stress power)이라 합니다. 단위 현재 부피당, 변형이 재료에 에너지를 넣는
비율입니다. 이후 내용으로 이어지는 통로이기도 해서,
[응력]({{< ref "stress.md" >}})은 이 값에 세 가지 표현이 있음을 보이고
[구성 방정식]({{< ref "constitutive.md" >}})은 이 항 때문에 에너지 함수를
미분해 응력을 얻을 수 있음을 보입니다.

## 미지수와 방정식을 세어 보면

지금까지 얻은 것은 질량에서 스칼라 방정식 하나, 선운동량에서 셋,
각운동량에서 대칭 제약, 에너지에서 스칼라 하나입니다.

열적 효과를 빼고 세어 보겠습니다. 미지수는
{{< katex >}}\rho{{< /katex >}} 하나,
{{< katex >}}\mathbf{v}{{< /katex >}} 셋,
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 여섯(대칭성 적용 후)으로 모두
열 개입니다. 방정식은 질량 하나와 운동량 셋으로 네 개입니다.

여섯 개가 모자랍니다. 보존 법칙을 더 파고들어도 이 간격은 메워지지 않습니다.
그 자리가 바로 재료를 아직 정하지 않은 자리이기 때문입니다. 메우는 일은
[구성 방정식]({{< ref "constitutive.md" >}})의 몫입니다.

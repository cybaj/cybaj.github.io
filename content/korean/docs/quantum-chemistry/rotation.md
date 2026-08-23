---
title: 회전 운동과 각운동량
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 50
item: 2026-08-23-quantum-chemistry
---

앞의 두 문제에서 양자화는 언제나 가둠에서 나왔습니다. 상자는 벽으로
가뒀고([상자 속 입자]({{< ref "particle-in-a-box.md" >}})), 조화 진동자는
무한히 높아지는 퍼텐셜로 가뒀습니다([조화 진동자]({{< ref "oscillator.md" >}})).

이번에는 가두지 않습니다. 퍼텐셜이 아예 0 인데도 양자화가 일어나는데, 어떻게
그럴 수 있는지가 문제이고 그 답이 원자의 구조로 곧장 이어집니다.
(개인 노트: 5장 회전 운동과 각운동량)

## 고리 위의 입자

가장 단순한 회전부터 보겠습니다. 반지름 {{< katex >}}r{{< /katex >}} 인 원
위를 도는 질량 {{< katex >}}m{{< /katex >}} 의 입자입니다. 반지름은
고정이므로 위치를 정하는 데는 각도 {{< katex >}}\phi{{< /katex >}} 하나면
충분합니다.

회전 운동에서는 질량 대신 관성 모멘트를 쓰는 편이 편합니다.

{{< katex display=true >}}
I = mr^2
{{< /katex >}}

직선 운동의 {{< katex >}}p^2/2m{{< /katex >}} 에 대응하는 회전 운동에너지가
{{< katex >}}l_z^2/2I{{< /katex >}} 이므로, Hamiltonian 은 각도에 대한
미분으로 쓰입니다.

{{< katex display=true >}}
\boxed{\;-\frac{\hbar^2}{2I}\frac{d^2\psi}{d\phi^2} = E\psi\;}
{{< /katex >}}

오른쪽에 퍼텐셜 항이 없다는 점을 눈여겨볼 만합니다. 입자는 고리 위를
자유롭게 돌고, 어느 각도가 다른 각도보다 유리하지도 않습니다. 형태만 보면
[자유입자]({{< ref "particle-in-a-box.md" >}}) 방정식과 똑같은데, 자유입자는
양자화되지 않았습니다.

그런데 이번에는 양자화됩니다.

## 되돌아옴이라는 조건

차이는 공간의 모양에 있습니다. 직선은 끝없이 뻗지만 원은 한 바퀴 돌면
제자리로 돌아옵니다.

각도 {{< katex >}}\phi{{< /katex >}} 와 각도
{{< katex >}}\phi + 2\pi{{< /katex >}} 는 서로 다른 숫자이지만 같은 지점을
가리킵니다. 파동함수는 위치의 함수이므로 같은 지점에서 두 값을 가질 수
없습니다.
([파동함수와 Schrödinger 방정식]({{< ref "wavefunction.md" >}})의 조건 2,
일가함수여야 한다는 조건이 바로 이것입니다.) 따라서

{{< katex display=true >}}
\boxed{\;\psi(\phi + 2\pi) = \psi(\phi)\;}
{{< /katex >}}

이어야 합니다. 이것을 **순환 경계조건**(cyclic boundary condition)이라
합니다.

벽이 없어도 조건은 있습니다. 갇혀서가 아니라 되돌아와서 생긴 조건입니다.

## 다시 정수가 나온다

방정식의 해는 자유입자와 같은 꼴입니다.

{{< katex display=true >}}
\psi(\phi) = N e^{im_l\phi}
{{< /katex >}}

넣어서 확인하면

{{< katex display=true >}}
\frac{d^2}{d\phi^2}e^{im_l\phi} = -m_l^2 e^{im_l\phi}
{{< /katex >}}

이므로 방정식이 만족되고 에너지는
{{< katex >}}E = m_l^2\hbar^2/2I{{< /katex >}} 가 됩니다. 아직
{{< katex >}}m_l{{< /katex >}} 에는 아무 제약이 없습니다.

이제 순환 조건을 걸어 보겠습니다.

{{< katex display=true >}}
e^{im_l(\phi+2\pi)} = e^{im_l\phi}
{{< /katex >}}

양변을 {{< katex >}}e^{im_l\phi}{{< /katex >}} 로 나누면

{{< katex display=true >}}
e^{2\pi i m_l} = 1
{{< /katex >}}

Euler 공식 {{< katex >}}e^{i\theta} = \cos\theta + i\sin\theta{{< /katex >}} 로
풀어 쓰면

{{< katex display=true >}}
\cos(2\pi m_l) + i\sin(2\pi m_l) = 1
{{< /katex >}}

이려면 {{< katex >}}\cos(2\pi m_l) = 1{{< /katex >}} 이고
{{< katex >}}\sin(2\pi m_l) = 0{{< /katex >}} 이어야 하는데, 이 둘을 동시에
만족하는 것은 {{< katex >}}m_l{{< /katex >}} 이 정수일 때뿐입니다.

{{< katex display=true >}}
\boxed{\;m_l = 0, \pm1, \pm2, \dots\;}
{{< /katex >}}

벽이 하나도 없는데 정수가 나왔습니다. 상자에서는 사인의 영점이 띄엄띄엄해서
나왔고, 여기서는 지수함수가 한 바퀴 뒤에 원래 값으로 돌아오는 지점이
띄엄띄엄해서 나왔습니다. 조건의 출처는 다르지만 결과는 같습니다.

{{< katex >}}m_l{{< /katex >}} 이 음수도 될 수 있다는 점은 상자와 다릅니다.
부호는 회전 방향을 뜻해서, 양수면 한 방향이고 음수면 반대 방향입니다.
{{< katex >}}m_l = 0{{< /katex >}} 은 회전하지 않는 상태인데, 상자와 달리
이것은 허용됩니다. 파동함수가 {{< katex >}}\psi = N{{< /katex >}} 인 상수여서
0 이 아니기 때문입니다.

## 에너지와 각운동량

에너지는

{{< katex display=true >}}
\boxed{\;E_{m_l} = \frac{m_l^2\hbar^2}{2I}\;}
{{< /katex >}}

이고 {{< katex >}}m_l{{< /katex >}} 의 제곱에 비례하므로
{{< katex >}}\pm m_l{{< /katex >}} 두 상태의 에너지가 같습니다. 어느 방향으로
돌든 에너지는 같다는 뜻이고, 이것도 겹침입니다.

각운동량은 조금 더 흥미롭습니다.
{{< katex >}}z{{< /katex >}} 축 각운동량 연산자는

{{< katex display=true >}}
\hat{l}_z = -i\hbar\frac{d}{d\phi}
{{< /katex >}}

인데, 이것을 우리 파동함수에 작용시키면

{{< katex display=true >}}
\hat{l}_z\psi_{m_l} = -i\hbar\,(im_l)\,Ne^{im_l\phi} = m_l\hbar\,\psi_{m_l}
{{< /katex >}}

파동함수가 그대로 나옵니다. 즉
{{< katex >}}\psi_{m_l}{{< /katex >}} 은
{{< katex >}}\hat{l}_z{{< /katex >}} 의 고유함수이고, 고윳값이

{{< katex display=true >}}
\boxed{\;l_z = m_l\hbar\;}
{{< /katex >}}

입니다. [파동함수 문서]({{< ref "wavefunction.md" >}})에서 본 대로
고유상태에서는 그 물리량이 확정값을 가지므로, 이 상태에서 각운동량을 재면
언제나 정확히 {{< katex >}}m_l\hbar{{< /katex >}} 가 나옵니다.

각운동량은 {{< katex >}}\hbar{{< /katex >}} 를 단위로 띄엄띄엄합니다. 에너지가
양자화된 것과는 별개이면서 더 근본적인 사실입니다.
{{< katex >}}\hbar{{< /katex >}} 의 단위가 실제로 각운동량의 단위(J·s)인 것도
우연이 아닙니다.

## 각도는 완전히 모른다

확률밀도를 구해 보면 재미있는 일이 벌어집니다.

{{< katex display=true >}}
|\psi_{m_l}(\phi)|^2 = \psi^*\psi
= \frac{1}{\sqrt{2\pi}}e^{-im_l\phi}\cdot\frac{1}{\sqrt{2\pi}}e^{im_l\phi}
= \frac{1}{2\pi}
{{< /katex >}}

지수가 상쇄되어 각도에 전혀 의존하지 않는 상수가 됩니다. 입자가 고리 위
어디에 있을 확률이 모두 같다는 뜻입니다.

각운동량을 정확히 아는 대가로 위치를 완전히 잃은 셈입니다. 직선 운동에서
운동량을 정확히 알면 위치를 모르는 것과 같은 구조이며, 각도와 각운동량
사이에도

{{< katex display=true >}}
\Delta \phi\,\Delta l_z \gtrsim \hbar
{{< /katex >}}

의 관계가 성립합니다.

## 구면 위의 입자

이제 3차원으로 넘어가겠습니다. 반지름이 고정된 구면 위를 도는 입자입니다.
원자 속 전자를 생각하면 이것이 필요한 이유가 분명해집니다. 전자는 평면이
아니라 공간에서 핵 주위를 돌기 때문입니다.

각도는 둘이 필요합니다. 위도에 해당하는
{{< katex >}}\theta{{< /katex >}} 와 경도에 해당하는
{{< katex >}}\phi{{< /katex >}} 입니다. 방정식은 각도에 대한 2차 미분이 둘
있는 꼴이 됩니다.

{{< katex display=true >}}
-\frac{\hbar^2}{2I}\left[
\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)
+ \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}
\right] Y(\theta,\phi) = E\,Y(\theta,\phi)
{{< /katex >}}

생긴 것은 복잡하지만 하는 일은 같습니다. 이번에는 순환 조건이 두 개 생기므로
양자수도 두 개 나옵니다.

{{< katex display=true >}}
\boxed{\;l = 0, 1, 2, \dots \qquad m_l = 0, \pm1, \dots, \pm l\;}
{{< /katex >}}

{{< katex >}}m_l{{< /katex >}} 이 {{< katex >}}l{{< /katex >}} 을 넘지 못한다는
제약이 새로 붙었는데, 그 의미는 곧 보겠습니다.

해는 **구면조화함수**(spherical harmonics)
{{< katex >}}Y_l^{m_l}(\theta,\phi){{< /katex >}} 라 불리는 함수들이고,
에너지는

{{< katex display=true >}}
\boxed{\;E_l = \frac{l(l+1)\hbar^2}{2I}\;}
{{< /katex >}}

입니다. 고리에서는 {{< katex >}}m_l^2{{< /katex >}} 이었는데 구면에서는
{{< katex >}}l(l+1){{< /katex >}} 이 되었습니다.

### 겹침

에너지가 {{< katex >}}l{{< /katex >}} 에만 의존하고
{{< katex >}}m_l{{< /katex >}} 에는 의존하지 않습니다. 그런데 각
{{< katex >}}l{{< /katex >}} 마다 {{< katex >}}m_l{{< /katex >}} 이
{{< katex >}}-l{{< /katex >}} 부터 {{< katex >}}+l{{< /katex >}} 까지
{{< katex >}}2l+1{{< /katex >}} 개 있으므로

{{< katex display=true >}}
\text{겹침 수} = 2l + 1
{{< /katex >}}

입니다. 이유는 [정사각형 상자]({{< ref "particle-in-a-box.md" >}})에서와
같은 대칭성입니다. 아무것도 없는 공간에는 특별한 방향이 없으므로 회전축이 어느
쪽을 향하든 에너지가 같을 수밖에 없습니다. 자기장을 걸어 한 방향을 특별하게
만들면 이 겹침이 풀립니다(Zeeman 효과).

## 각운동량의 크기와 방향

구면에서 각운동량의 크기와 {{< katex >}}z{{< /katex >}} 성분은

{{< katex display=true >}}
|\mathbf{l}| = \sqrt{l(l+1)}\,\hbar,
\qquad
l_z = m_l\hbar
{{< /katex >}}

입니다. 여기에는 처음 보면 대개 걸리는 지점이 하나 있습니다.

{{< katex >}}m_l{{< /katex >}} 의 최댓값은 {{< katex >}}l{{< /katex >}} 인데
크기는 {{< katex >}}\sqrt{l(l+1)}{{< /katex >}} 이고, 언제나

{{< katex display=true >}}
l < \sqrt{l(l+1)}
{{< /katex >}}

입니다. {{< katex >}}z{{< /katex >}} 성분이 아무리 커도 전체 크기에는 미치지
못한다는 뜻이고, 각운동량 벡터를 {{< katex >}}z{{< /katex >}} 축에 완전히
나란히 세울 수 없다는 뜻이기도 합니다.

이유는 이렇습니다. 만약 벡터가 정확히 {{< katex >}}z{{< /katex >}} 축을
향한다면 {{< katex >}}l_x = l_y = 0{{< /katex >}} 이 확정됩니다. 그런데
각운동량의 세 성분은 서로 불확정성 관계에 있어 둘 이상을 동시에 확정할 수
없고, 하나를 확정하면 나머지 둘은 흐려져야 합니다. 벡터가 축에서 조금
기울어 있는 것은 그 흐림의 기하학적 표현입니다.

숫자로 보면 더 분명합니다. {{< katex >}}l = 1{{< /katex >}} 일 때 크기는
{{< katex >}}\sqrt{2}\hbar \approx 1.41\hbar{{< /katex >}} 인데
{{< katex >}}l_z{{< /katex >}} 의 최댓값은 {{< katex >}}\hbar{{< /katex >}}
입니다. 각도로는

{{< katex display=true >}}
\cos\alpha = \frac{l_z}{|\mathbf{l}|} = \frac{1}{\sqrt{2}}
\qquad \Longrightarrow \qquad
\alpha = 45^\circ
{{< /katex >}}

가장 많이 정렬시켜도 45도가 한계입니다.

## 마디와 오비탈의 모양

구면조화함수도 마디를 갖습니다. 상자와 진동자에서는 마디가 점이었지만
구면에서는 면입니다. 각도 마디의 수는

{{< katex display=true >}}
\text{각도 마디 수} = l
{{< /katex >}}

입니다. {{< katex >}}l = 0{{< /katex >}} 이면 마디가 없어 어느 방향으로나
같은 값을 갖는 구형이 되고, {{< katex >}}l = 1{{< /katex >}} 이면 마디면이
하나라 아령 모양, {{< katex >}}l = 2{{< /katex >}} 면 둘이라 네 잎 모양이
됩니다.

이 모양들에는 이름이 붙어 있습니다.

| {{< katex >}}l{{< /katex >}} | 이름 | 각도 마디 | 겹침 |
|---|---|---|---|
| 0 | {{< katex >}}s{{< /katex >}} | 0 | 1 |
| 1 | {{< katex >}}p{{< /katex >}} | 1 | 3 |
| 2 | {{< katex >}}d{{< /katex >}} | 2 | 5 |
| 3 | {{< katex >}}f{{< /katex >}} | 3 | 7 |

여기서 회전 문제가 원자로 이어집니다. 수소 원자를 풀면 퍼텐셜이 구대칭이라는
이유만으로 해가 반지름 부분과 각도 부분으로 갈라지는데, 그 각도 부분이 바로
지금 구한 {{< katex >}}Y_l^{m_l}{{< /katex >}} 입니다.

다시 말해 오비탈의 모양은 이미 여기서 결정된 셈입니다. 수소 원자를 풀 때
{{< katex >}}s, p, d{{< /katex >}} 오비탈의 모양을 새로 계산할 필요가
없습니다. 전자가 핵에 어떻게 끌리는지와 무관하게, 공간이 구대칭이라는
사실만으로 정해지기 때문입니다.

## 숫자로 확인하기

분자의 회전은 상온에서 얼어 있지 않습니다.
[조화 진동자]({{< ref "oscillator.md" >}})에서는 진동의 준위 간격이 상온의
열에너지보다 훨씬 커서 얼어 있었는데, 회전은 어떤지 보겠습니다.

CO 분자를 예로 들겠습니다. 결합 길이 113 pm, 환산질량

{{< katex display=true >}}
\mu = \frac{(12.00)(15.99)}{12.00+15.99} = 6.856\ \mathrm{amu} = 1.139\times10^{-26}\ \mathrm{kg}
{{< /katex >}}

관성 모멘트는

{{< katex display=true >}}
I = \mu r^2 = (1.139\times10^{-26})(1.13\times10^{-10})^2
= 1.45\times10^{-46}\ \mathrm{kg\,m^2}
{{< /katex >}}

가장 낮은 전이 {{< katex >}}l = 0 \to 1{{< /katex >}} 의 에너지는

{{< katex display=true >}}
\Delta E = \frac{1(1+1)\hbar^2}{2I} - 0 = \frac{\hbar^2}{I}
= \frac{(1.055\times10^{-34})^2}{1.45\times10^{-46}}
= 7.7\times10^{-23}\ \mathrm{J}
{{< /katex >}}

{{< katex >}}0.48\ \mathrm{meV}{{< /katex >}} 입니다. 상온의
{{< katex >}}kT = 25.7\ \mathrm{meV}{{< /katex >}} 와 비교하면 50 배 이상
작습니다.

{{< katex display=true >}}
\frac{\Delta E}{kT} \approx 0.019 \ll 1
{{< /katex >}}

회전 준위는 상온에서 골고루 채워져 있습니다. 같은 분자에서도 진동은 얼어
있고 회전은 활발한, 자유도마다 다른 답이 나오는 상황입니다. 기체의 열용량이
온도에 따라 계단식으로 변하는 이유가 여기에 있습니다. 낮은 온도에서는 병진만
참여하고, 온도를 올리면 회전이, 더 올리면 진동이 참여합니다.

파장으로 보면 이 전이는 마이크로파 영역에 있습니다. 회전 스펙트럼을 마이크로파
분광법으로 재는 이유이고, 전자레인지가 물 분자를 돌리는 것도 같은 영역의
이야기입니다.

**각운동량의 크기.** {{< katex >}}l = 2{{< /katex >}} 인
{{< katex >}}d{{< /katex >}} 오비탈에서

{{< katex display=true >}}
|\mathbf{l}| = \sqrt{2\cdot3}\,\hbar = \sqrt{6}\,\hbar = 2.45\hbar
{{< /katex >}}

인데 {{< katex >}}l_z{{< /katex >}} 는
{{< katex >}}-2\hbar, -\hbar, 0, \hbar, 2\hbar{{< /katex >}} 다섯 값만
가집니다.
최대로 정렬해도 {{< katex >}}2\hbar < 2.45\hbar{{< /katex >}} 이므로

{{< katex display=true >}}
\cos\alpha = \frac{2}{\sqrt{6}} = 0.816
\qquad \Longrightarrow \qquad
\alpha = 35.3^\circ
{{< /katex >}}

{{< katex >}}l{{< /katex >}} 이 커질수록 최대 정렬 각도가 작아지지만 0 이
되지는 않습니다. {{< katex >}}l \to \infty{{< /katex >}} 에서
{{< katex >}}l/\sqrt{l(l+1)} \to 1{{< /katex >}} 이므로 고전적인 "축에 나란한
회전"이 극한에서 회복되는, 또 한 번의 대응원리입니다.

이것으로 세 개의 모형 문제가 끝났습니다. 벽에서 0 이 될 것, 무한히 멀리서 0
으로 수렴할 것, 한 바퀴 뒤에 같은 값이 될 것. 조건은 서로 달랐지만 세 경우
모두 허용되는 해가 띄엄띄엄해졌습니다. 실제 원자의 전자는 Coulomb 퍼텐셜에
묶여 있으면서 동시에 핵 주위를 돌기 때문에 반지름 조건과 각도 조건이 함께
걸리는데, 그 문제를 [수소꼴 원자]({{< ref "hydrogen.md" >}})에서
다루겠습니다.
